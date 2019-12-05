
.. _PYSOURCEINFO_BININFO:

sourceinfo.bininfo
******************

This modules provides for the location of Python execution
by means of the package 'inspect' extended by additional sources
for a simple API.

The stack frame of inspect is in particular reduced to the common
parameter *spos*, which is an abstraction of the 'stack-position'
representing the level of history within the caller level.
The value *spos==0* is the function itself, whereas *spos==1* is the
first level caller. Consequently *spos==2* is the caller of the caller,
etc.

The categories of provided RTTI comprise:

* **packages** - Python packages.

* **modules** - Python modules - a.k.a. source files.

* **callers** - Python functions and class/object methods.

The following definiton is applied: ::

   A package is represented by an imported top-entity which could either be a self-contained
   module, or the *__init__.py* special module as the top-entity from a set of modules within
   a sub directory structure.

So physically a package is a distribution unit, which provides one or more 
modules. Thus the displayed result in case of packages is the module when a self-contained,
the path when a multi-module package.

Where the following attributes are available:__

* name(package, module, function)

* OID - dotted relative path to matching item of sys.path

* filename

* filepathname

* item of sys.path

* relative path to item of sys.path

* line number

Dependent on the call context, some of the attribute values may
not be available.
E.g. when called from within the python/ipython shell, or 'main'.

The API is designed here as a collection of slim functions
only in order to avoid any overhead for generic application.

Modules
-------

.. automodule:: sourceinfo.bininfo

Functions
---------

.. _def_getcaller_bin_filename:

getcaller_bin_filename
^^^^^^^^^^^^^^^^^^^^^^

.. autofunction:: getcaller_bin_filename

.. _def_getcaller_bin_filepathname:

getcaller_bin_filepathname
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. autofunction:: getcaller_bin_filepathname

.. _def_getcaller_bin_pathname:

getcaller_bin_pathname
^^^^^^^^^^^^^^^^^^^^^^
.. autofunction:: getcaller_bin_pathname

.. _def_getcaller_bin_pathname_rel:

getcaller_bin_pathname_rel
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. autofunction:: getcaller_bin_pathname_rel

.. _def_getcaller_bin_pathname_sub:

getcaller_bin_pathname_sub
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. autofunction:: getcaller_bin_pathname_sub

.. _def_getmodule_bin_filename:

getmodule_bin_filename
^^^^^^^^^^^^^^^^^^^^^^
.. autofunction:: getmodule_bin_filename

.. _def_getmodule_bin_filepathname:

getmodule_bin_filepathname
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. autofunction:: getmodule_bin_filepathname

.. _def_getmodule_bin_pathname:

getmodule_bin_pathname
^^^^^^^^^^^^^^^^^^^^^^
.. autofunction:: getmodule_bin_pathname

.. _def_getmodule_bin_pathname_rel:

getmodule_bin_pathname_rel
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. autofunction:: getmodule_bin_pathname_rel

.. _def_getmodule_bin_pathname_sub:

getmodule_bin_pathname_sub
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. autofunction:: getmodule_bin_pathname_sub

Exceptions
----------


Resources
---------
* inspect Python2 - [inspect2]_
* inspect Python3 - [inspect3]_
* types Python2 - [types2]_
* types Python3 - [types3]_
* pystackinfo package; Arno-Can Uestuensoez [pystackinfo]_

