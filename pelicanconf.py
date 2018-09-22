
import shutil
import logging

AUTHOR = 'Marek Zdzislaw Szymanski'
M_SITE_LOGO_TEXT = 'oedes'
SITENAME = 'oedes'
SITEURL = ''
STATIC_URL = '{path}'
PATH = 'content'
ARTICLE_PATHS = ['examples']
ARTICLE_EXCLUDES = ['examples/authors', 'examples/categories', 'examples/tags']
PAGE_PATHS = ['']
TIMEZONE = 'Europe/Prague'
DEFAULT_LANG = 'en'
import platform
if platform.system() == 'Windows':
    DATE_FORMATS = {'en': ('usa', '%b %d, %Y')}
else:
    DATE_FORMATS = {'en': ('en_US.UTF-8', '%b %d, %Y')}
# Feed generation is usually not desired when developing
FEED_ATOM = None
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
M_BLOG_NAME = "oedes examples"
M_BLOG_URL = 'examples/'

M_METADATA_AUTHOR_PATH = 'examples/authors'
M_METADATA_CATEGORY_PATH = 'examples/categories'
M_METADATA_TAG_PATH = 'examples/tags'

M_LINKS_NAVBAR1 = [('Installation','/pages/installation/','pages/installation',[]),
                   ('Examples','/pages/examples/','pages/examples',[]),
                   ('Source code','https://github.com/mzszym/oedes','',[])]

M_LINKS_NAVBAR2 = []

M_LINKS_FOOTER1 = []
M_LINKS_FOOTER2 = []
M_LINKS_FOOTER3 = []
M_LINKS_FOOTER4 = []

M_FINE_PRINT = """
| oedes. Copyright © `Marek Szymanski <mzszym@gmail.com>`_, 2016--2018. Site
  powered by `Pelican <https://getpelican.com>`_ and `m.css <http://mcss.mosra.cz>`_.
"""
#M_FINE_PRINT = ""

DEFAULT_PAGINATION = 10

STATIC_PATHS = ['static']
#EXTRA_PATH_METADATA = {'static/favicon.ico': {'path': 'favicon.ico'}}

PLUGIN_PATHS = [ 'plugins', 'm.css/pelican-plugins' ]
PLUGINS = ['ipynb',
           'm.abbr',
           'm.code',
           'm.components',
           'm.dox',
           'm.dot',
           'm.filesize',
           'm.gl',
           'm.gh',
           'm.htmlsanity',
           'm.images',
           'm.link',
           'm.math',
           'm.metadata',
           'm.plots',
           'm.vk']

THEME = 'm.css/pelican-theme'
THEME_STATIC_DIR = 'static'
M_THEME_COLOR = '#22272e'
M_CSS_FILES = ['https://fonts.googleapis.com/css?family=Source+Code+Pro:400,400i,600%7CSource+Sans+Pro:400,400i,600,600i&subset=latin-ext',
               'static/m-dark.css',
              ]

FORMATTED_FIELDS = ['summary', 'landing', 'header', 'footer', 'description', 'badge']

M_HTMLSANITY_SMART_QUOTES = True
M_HTMLSANITY_HYPHENATION = True

if not shutil.which('latex'):
    logging.warning("LaTeX not found, fallback to rendering math as code")
    M_MATH_RENDER_AS_CODE = True

DIRECT_TEMPLATES = ['archives']

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
ARCHIVES_URL = 'examples/'
ARCHIVES_SAVE_AS = 'examples/index.html'
ARTICLE_URL = '{slug}/' # category is part of the slug (i.e., examples)
ARTICLE_SAVE_AS = '{slug}/index.html'
AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'

#AUTHORS_SAVE_AS = None # Not used
#CATEGORIES_SAVE_AS = None # Not used
#TAGS_SAVE_AS = None # Not used

SLUGIFY_SOURCE = 'basename'
PATH_METADATA = '(?P<slug>.+).rst'
