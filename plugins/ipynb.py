from pelican import signals
from pelican.readers import BaseReader,RstReader
from docutils.writers.html4css1 import Writer
import nbformat
import m2r
import docutils
from pelican.utils import truncate_html_words
import string
import re
import os

def fixrst(text):
    math=re.compile(r'\$(.*?)\$')
    lines=list(text.splitlines())
    output=[]
    for prevline,line in zip([None]+lines[:-1],lines):
        if line and line==line[:1]*len(line) and prevline and len(line)>=len(prevline):
            output.append(line[0]*len(output[-1]))
            continue
        out=[]
        while True:
            match = math.search(line)
            if not match:
                break
            out.append(line[:match.span()[0]])
            line=line[match.span()[1]:]
            out.append(':math:`{}`'.format(match.group(1)))
        out.append(line)
        out = ''.join(out)
        # whole line
        if len(out)>=2 and out[:1].isalpha() and out[1]=='.':
            out = '\\' + out
        output.append(out)
    return '\n'.join(output)

def convert_markdown(md):
    return fixrst(m2r.convert(md))

def nb2rst(content):
    data=nbformat.reads(content, as_version=4)
    result = []
    cells = list(data.cells)
    summary = None
    for cell in cells:
        source = cell.source
        if cell.cell_type == 'markdown':
            if cell is cells[-1] and cell.source.find('open source')>=0:
                continue
            rst = convert_markdown(cell.source)
            result.append(rst)
            if summary is None:
                summary = rst
        elif cell.cell_type == 'code':
            result.append('.. code:: python')
            result.append('\n\t'.join(['']+list(cell.source.splitlines())+['']))
            for out in cell.outputs:
                if out.output_type == 'stream':
                    pass
                elif out.output_type == 'display_data':
                    for d in out.data:
                        if d.startswith('image/png') or d.startswith('image/jp'):
                            result.append('.. raw:: html\n\n\t<div class="notebook-image"><img src="data:%s;base64,%s"/></div>'%(d,''.join(out.data[d].splitlines())))
                        elif d.startswith('image/svg'):
                            svg=out.data[d][out.data[d].find('<svg'):]
                            result.append('.. raw:: html\n\n\t<div class="notebook-image">\n\t%s\n\t</div>'%('\n\t'.join(svg.splitlines())))
                elif out.output_type == 'execute_result':
                    pass
        result.append('')
    rst='\n'.join(result)
    return rst,summary

class NotebookReader(BaseReader):
    enabled = True

    file_extensions = ['ipynb']

    def read(self, filename):
        if filename.find('.ipynb_checkpoints')>0:
            raise ValueError('not processing %s'%filename)
        with open(filename,'rb') as f: 
            rst,summary=nb2rst(f.read())

        extra_params = {'initial_header_level': '2',
                        'syntax_highlight': 'short',
                        'input_encoding': 'utf-8',
                        'exit_status_level': 2,
                        'embed_stylesheet': False}
        user_params = self.settings.get('DOCUTILS_SETTINGS')
        if user_params:
            extra_params.update(user_params)

        #pub = docutils.core.Publisher(
        #    writer=Writer(), #TODO?
        #    source_class=docutils.io.StringInput,
        #    destination_class=docutils.io.StringOutput)
        #pub.set_components('standalone', 'restructuredtext', 'html')
        #pub.process_programmatic_settings(None, extra_params, None)
        #pub.set_source(source=rst)
        #pub.publish(enable_exit_status=True)

        #parts = pub.writer.parts
        
        parts = docutils.core.publish_parts(rst, writer_name='html')
        if summary is not None:
            summary = docutils.core.publish_parts(summary, writer_name='html')['body']
        meta=dict(category='examples',title=parts['title'],date='2017-11-01',summary=summary,slug=os.path.splitext(os.path.split(filename)[1])[0])
        return parts['body'], dict((k,self.process_metadata(k,meta[k])) for k in meta)

def add_reader(readers):
    readers.reader_classes['ipynb'] = NotebookReader

# This is how pelican works.
def register():
    signals.readers_init.connect(add_reader)

if __name__ == '__main__':
    import sys
    sys.stdout.write(nb2rst(sys.stdin.read())[0])
