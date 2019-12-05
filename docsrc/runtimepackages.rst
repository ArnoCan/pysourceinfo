
.. _RUNTIMEPACKAGES:

Runtime Packages
================

Python supports for multiple types of installation packages and runtime packages.
This chapter describes the runtime packages.

Package Types
-------------

Single File Packages
^^^^^^^^^^^^^^^^^^^^
The simplest form of a package is one python file, which contains 
library classes and/or functions.
This could be simply deployed by copying one file only and addressing it 
as a Python OID. 
The following module as a package named 'mypackage.py':

.. code-block:: python
   :linenos:

   def myLibFunc():
     return "here I am"

could be used as:

.. code-block:: python
   :linenos:

   import mypackage
   print mypackage.myLibFunc()


Multiple File Packages
^^^^^^^^^^^^^^^^^^^^^^
A package normally consists of more than one file only.
The files could be placed into one directory with and additional
file named *__init__.py* as a package consisting of multiple files.
The files are called 'module', and addressed by the common addressing schema.
This has no influence on the *PYTHONPATH*/*sys.path*
or the package path.
Thus are handled from the point of view of *pysourceinfo* as compoennts of 
a normal package with a path-prefix.


Subpackages
^^^^^^^^^^^
Packages contained within another package are called sub-packages.
The probably most prominent example is *os*,
which is imported mostly by the package itself

.. code-block:: python
   :linenos:

   import os

and addressed by it's qualified name

.. code-block:: python
   :linenos:

   os.path

The main characteristic is the hierarchical path in a containment tree structures. 
The property sub-package has no influence on the *PYTHONPATH*/*sys.path*
or the package path.
Thus could be handled from the point of view of *pysourceinfo* as a normal 
package with a path-prefix or simply as components of the main package.

Zip Archives as Runtime-Repositories
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The [PEP273]_ and the [PEP441]_ specifies the interface for loading modules from
zip-files.
The zipfile itself is partially transparent, which means it does not occur on 
the OID of the module path, while the zipfile name is part of the filename path
provided by the *__file__* attribute.

E.g. the file structure:

::

   +--test01
      |
      +--A
      |  |
      |  +--a.py
      |  +--__init__.py
      |
      +--test01.py
      +--__init__.py

Containing the file "test001.A.a.py":

.. code-block:: python
   :linenos:

   def func_a():
       return "func_a:"+__file__


and the file "test001.test001.py":

.. code-block:: python
   :linenos:

   def func_test01():
       return "func_test01:"+__file__
   def func():
       return "func:"+__file__

When zipped with the call:

.. code-block:: python
   :linenos:

   zip -r pkg_test01.zip test01

The contained code could now be imported and used as:

.. code-block:: python
   :linenos:

   from __future__ import print_function
   import sys,os

   #
   # sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))+
   #    os.path.sep+'pkg_test01.zip')
   #
   sys.path.insert(0,'pkg_test01.zip')
   print(sys.path[0])

   import test01.test01
   import test01.A.a

   print(test01.test01.func())
   print(test01.test01.func_test01())
   print(test01.A.a.func_a())

   print(test01.test01.__file__)
   print(test01.A.a.__file__)

   print(test01.test01.func.__name__)
   print(test01.test01.func_test01.__name__)
   print(test01.A.a.func_a.__name__)

Resulting in the output::

   [acue@lap001 zip-packages]$ python main.py
   pkg_test01.zip
   func:pkg_test01.zip/test01/test01.py
   func_test01:pkg_test01.zip/test01/test01.py
   func_a:pkg_test01.zip/test01/A/a.py
   pkg_test01.zip/test01/test01.py
   pkg_test01.zip/test01/A/a.py
   func
   func_test01
   func_a

The result shows, that the zipfile itself is neither contained in the 
file system path, while it is not part of the logical OID of the module path.
Thus the source code parts of the *pysourceinfo* package handle the zipfile
transparently too.
 
Implicit Namespace Packages
^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. The package is an implicit namespace package, [PEP420]_.

Runtime Binaries
----------------

PYC Repository Directories
^^^^^^^^^^^^^^^^^^^^^^^^^^ 



Resources
---------

* [PEP273]_ - Import Modules from Zip Archives 
* [PEP302]_ - New Import Hooks
* [PEP3147]_ - PYC Repository Directories
* [PEP3155]_ - Qualified name for classes and functions
* [PEP420]_ - Implicit Namespace Packages
* [PEP441]_ - Improving Python ZIP Application Support
* pystackinfo package; Arno-Can Uestuensoez [pystackinfo]_

