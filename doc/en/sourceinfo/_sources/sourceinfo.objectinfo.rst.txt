
.. _PYSOURCEINFO_OBJECTINFO:

sourceinfo.objectinfo
*********************

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

The following definiton is applied:

.. note::

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

.. automodule:: sourceinfo.objectinfo

Constants
---------

Re-Mapped *imp* Constants
^^^^^^^^^^^^^^^^^^^^^^^^^
Literally re-mapped constants from *imp* package for single import.
These are obsolete in imp with >=3.3, but continued within *PySourceInfo*. 

*  *MT_UNKNOWN = 0*
*  *MT_SOURCE = 1* # imp.PY_SOURCE
*  *MT_COMPILED = 2* # imp.PY_COMPILED
*  *MT_EXTENSION = 3* # imp.C_EXTENSION
*  *MT_DIRECTORY = 5* # imp.PKG_DIRECTORY
*  *MT_BUILTIN = 6* # imp.C_BUILTIN
*  *MT_FROZEN = 7* # imp.PY_FROZEN

Functions
---------

.. _def_getcaller_module:

getcaller_module
^^^^^^^^^^^^^^^^
.. autofunction:: getcaller_module

.. _def_getcaller_module_name:

getcaller_module_name
^^^^^^^^^^^^^^^^^^^^^
.. autofunction:: getcaller_module_name 	 

.. _def_getcaller_module_name_sub:

getcaller_module_name_sub
^^^^^^^^^^^^^^^^^^^^^^^^^
.. autofunction:: getcaller_module_name_sub
    
.. _def_getcaller_module_oid:

getcaller_module_oid
^^^^^^^^^^^^^^^^^^^^
.. autofunction:: getcaller_module_oid

.. _def_getcaller_module_oid_sub:

getcaller_module_oid_sub
^^^^^^^^^^^^^^^^^^^^^^^^
.. autofunction:: getcaller_module_oid_sub


.. _def_getcaller_name:

getcaller_name
^^^^^^^^^^^^^^
.. autofunction:: getcaller_name
    

.. _def_getcaller_package_name:

getcaller_package_name
^^^^^^^^^^^^^^^^^^^^^^
.. autofunction:: getcaller_package_name
    

.. _def_getmodule_by_id:

getmodule_by_id
^^^^^^^^^^^^^^^
.. autofunction:: getmodule_by_id

.. _def_getmodule_by_name:

getmodule_by_name
^^^^^^^^^^^^^^^^^
.. autofunction:: getmodule_by_name

.. _def_getmodule_name:

getmodule_name
^^^^^^^^^^^^^^
.. autofunction:: getmodule_name

.. _def_getmodule_name_sub:

getmodule_name_sub
^^^^^^^^^^^^^^^^^^
.. autofunction:: getmodule_name_sub


.. _def_getmodule_oid:

getmodule_oid
^^^^^^^^^^^^^
.. autofunction:: getmodule_oid
    

.. _def_getmodule_oid_sub:

getmodule_oid_sub
^^^^^^^^^^^^^^^^^
.. autofunction:: getmodule_oid_sub
    

.. _def_getmodule_package_name:

getmodule_package_name
^^^^^^^^^^^^^^^^^^^^^^
.. autofunction:: getmodule_package_name


.. _def_getmodule_type:

getmodule_type
^^^^^^^^^^^^^^
.. autofunction:: getmodule_type


Exceptions
----------


Resources
---------
* inspect Python2 - [inspect2]_
* inspect Python3 - [inspect3]_
* pystackinfo package; Arno-Can Uestuensoez [pystackinfo]_
* types Python2 - [types2]_
* types Python3 - [types3]_
