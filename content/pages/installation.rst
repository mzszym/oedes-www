Installation
============

Requirements
------------

- Python 2.7 or Python 3.4+
- sparsegrad
- Python scientific stack

Installation from PyPI
----------------------

This is the preferred way of installing ``oedes``. It automatically takes care of all dependencies.

Two variants of the installation are possible:

- system wide installation:

.. code-block:: bash

   $ pip install oedes

- local installation not requiring administrator's rights:

.. code-block:: bash

   $ pip install oedes --user

In the case of local installation, ``oedes`` is installed inside user's home directory. In Linux, this defaults to ``$HOME/.local``.

Development installation (advanced)
-----------------------------------

Current development version of sparsegrad can be installed from the development repository by running

.. code-block:: bash

   $ git clone https://github.com/mzszym/oedes.git
   $ cd oedes
   $ pip install -e .

The option ``-e`` tells that ``oedes`` code should be loaded from ``git`` controlled directory, instead of being copied to the Python libraries directory. As with the regular installation, ``--user`` option should be appended for local installation.


