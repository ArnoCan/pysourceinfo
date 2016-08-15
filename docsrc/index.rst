

.. pysourceinfo documentation master file, created by
   sphinx-quickstart on `date`.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Abstract
========

The 'pysourceinfo' package provides basic runtime information on executed sourcefiles
based on 'inspect' and additional sources `[shortcuts] <shortcuts.html#>`_.


* **Runtime Type Information on Packages, Modules, and Calls**

  A basic coverage of the 'inspect' package is provided for the 
  simplified gathering of information on packages, modules, and files based 
  on the call stack.

  * Python source information: 
    `Python Source Structures <sourceinfo.html>`_ 

  * Programming Interface: 
    `[shortcuts] <shortcuts.html#pysourceinfo-pysourceinfo>`_
    `[API] <epydoc/index.html>`_

    .

The provided feature modules comprise the following list.

* `PySourceInfo <pysourceinfo.html>`_ : 
     Provides runtime type information on Python source components: packages, modules, and callers  - *pysourceinfo.PySourceInfo*.

For code examples refer to the souce code of 'pysourceinfo.UseCases' 
and 'pysourceinfo.tests'.


`Shortcuts <shortcuts.html>`_
=============================

Common Interfaces:

* `Programming Interface <shortcuts.html#>`_

Complete technical API:

* `API by Epydoc <epydoc/index.html>`_

Table of Contents
=================
.. toctree::
   :maxdepth: 3

   shortcuts
   pysourceinfo
   UseCases
   tests
   testdata

* setup.py

  For help on extensions to standard options call onlinehelp:: 

    python setup.py --help-pysourceinfo



Indices and tables
==================


* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


Resources
=========

For available downloads refer to:

* Python Package Index: https://pypi.python.org/pypi/pysourceinfo

* Sourceforge.net: https://sourceforge.net/projects/pysourceinfo/

* github.com: https://github.com/ArnoCan/pysourceinfo/

For Licenses refer to enclosed documents:

* Artistic-License-2.0(base license): `ArtisticLicense20.html <_static/ArtisticLicense20.html>`_

* Forced-Fairplay-Constraints(amendments): `licenses-amendments.txt <_static/licenses-amendments.txt>`_ / `Protect OpenSource Authors <http://xkcd.com/1303/>`_

