Abstract
========

The 'pysourceinfo' package provides basic runtime information on executed sourcefiles
based on 'inspect' and additional sources `[shortcuts] <shortcuts.html#>`_.


* **Runtime Type Information on Python source components: Packages, Modules, and Calls**

  A basic coverage of the 'inspect' package is provided for the 
  simplified gathering of information on packages, modules, and files based 
  on the call stack 
  `[details] <sourceinfo.html>`_ 

  * **callers** - Python functions and class/object methods
    :ref:`[API-selection] <CallerFunctionsandMethods>`.

  * **modules** - Python modules - a.k.a. source files
    :ref:`[API-selection] <CallerModulesFiles>`.

  * **packages** - Python packages based on 'inspect'
    :ref:`[API-selection] <CallerPackagesFilesandorDirectories>`
    or based on 'sys.path'
    :ref:`[API-selection] <CallerPackagesFilesandorDirectoriesSysPath>`.

  .
The main target of the project is the completion and simplification of the call interface 
for the most common calls related to RTTI provided by 'inspect'.

Blueprint
=========

The features provided by the package 'pysourceinfo' are
based on the standard package 'inspect' with
dynamic evaluation of additional sources where rewuired.
A flat call interface is provided for simplified application in
OO as well as simple scripting.

The provided runtime structure information on Python sources is 
covered with basically one single type of interface
  ::

    def getCaller<Interface>(spos=1):
       """ Stack position: 
          spos==0 => caller(0==CallInterface) 
          spos==1 => caller(1) 
          spos==N => caller(N==level N) 
       """
       pass

    def getModule<Interface>(spos=1):
       pass

    def getPythonPath<Interface>(spos=1):
       pass

The interface gathers the information on the defined '<Interface>' from
the call stack, loaded modules, or search path 'PATH'/'PYTHONPATH'/'sys.path'.

The covered structural dynamic elements based on the call stackk are:

* package

* module

* function

* class/method

* namespaces - global/local

With additional functions covering mostly static information: 

* loaded module

* sys.path - actual OID and load path

For code and application examples refer to the souce code of 'pysourceinfo.UseCases' `[UseCases] <UseCases.html#>`_
and 'pysourceinfo.tests' `[tests] <tests.html#>`_.

Install - HowTo - FAQ - Help
============================

* **Install**:

  Standard procedure online local install by sources::

    python setup.py install --user

  Custom procedure offline by::

    python setup.py install --user --offline

  Documents, requires Sphinx and Epydoc::

    python setup.py build_doc install_doc

* **Help**:

  **Remark**: On Windows platforms it seems to be required the inspect module has to be
  initialized, so for now please include befor the import of 'pysourceinfo'::

    # For now a dummy call for initialization, will be cleared soon...
    import inspect
    _dummyInit = inspect.stack()

    # For example...
    from pysourceinfo.PySourceInfo import getCallerModule,getCallerName

  that's it. Going to investigate this soon.

`Shortcuts <shortcuts.html>`_
=============================

Common Interfaces:

* `Programming Interface <shortcuts.html#>`_

Complete technical API:

* Interface in javadoc-style `[API] <epydoc/index.html>`_

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

