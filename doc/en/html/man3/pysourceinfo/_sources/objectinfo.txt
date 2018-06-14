'pysourceinfo.objectinfo' - Module
**********************************

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

.. automodule:: pysourceinfo.objectinfo

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

getcaller_module
^^^^^^^^^^^^^^^^
	.. autofunction:: getcaller_module

           Args:

             spos: Caller position on the stack.

           Returns:

             Returns the caller module.

           Raises:

             passed through exceptions

getcaller_module_name
^^^^^^^^^^^^^^^^^^^^^
	.. autofunction:: getcaller_module_name 
    
           Both approaches for evaluation the actual relative
           module name seem to have their own challenges,
           *module.__name__* and *getmodule_name()*.

           Args:

             spos: Caller position on the stack.

           Returns:

             Returns the name of caller module.
             The dotted object path is relative to
             the actual used sys.path item.

           Raises:

             passed through exceptions

getcaller_module_name_sub
^^^^^^^^^^^^^^^^^^^^^^^^^
	.. autofunction:: getcaller_module_name_sub
    
           Args:

             spos: Caller position on the stack.

           Returns:

             Returns the sub-name as the portion from package to module.

           Raises:

             passed through exceptions

getcaller_module_oid
^^^^^^^^^^^^^^^^^^^^
	.. autofunction:: getcaller_module_oid

           Args:

             spos: Caller position on the stack.

           Returns:

             Returns the OID of the module.

           Raises:

             passed through exceptions

getcaller_module_oid_sub
^^^^^^^^^^^^^^^^^^^^^^^^
	.. autofunction:: getcaller_module_oid_sub

           Args:

             spos: Caller position on the stack.

           Returns:

             Returns the sub-OID of the module.

           Raises:

             passed through exceptions

getcaller_name
^^^^^^^^^^^^^^
	.. autofunction:: getcaller_name
    
           Args:

             spos: Caller position on the stack.

           Returns:

             Returns the name.

           Raises:

             passed through exceptions

getcaller_package_name
^^^^^^^^^^^^^^^^^^^^^^
	.. autofunction:: getcaller_package_name
    
           Relies on 'inspect'.
    
           Args:

             spos: Caller position on the stack.

           Returns:

             Returns the package name when defined, else None.

           Raises:

             passed through exceptions

getmodule_by_id
^^^^^^^^^^^^^^^
	.. autofunction:: getmodule_by_id

           Args:

             n: ID of loaded module.

           Returns:

             Returns the loaded module.

           Raises:

             passed through exceptions

getmodule_by_name
^^^^^^^^^^^^^^^^^
	.. autofunction:: getmodule_by_name

           Args:

             n: Name of the loaded module.

           Returns:

             Returns the loaded module.

           Raises:

             passed through exceptions

getmodule_name
^^^^^^^^^^^^^^
	.. autofunction:: getmodule_name

           Args:

             mod: Module.

           Returns:

             Returns the name of the loaded module.

           Raises:

             passed through exceptions

getmodule_name_sub
^^^^^^^^^^^^^^^^^^
	.. autofunction:: getmodule_name_sub

           Args:

             mod: Module.

           Returns:

             Returns the sub-name of the loaded module.

           Raises:

             passed through exceptions

getmodule_oid
^^^^^^^^^^^^^
	.. autofunction:: getmodule_oid
    
           Args:

             mod: Module.

           Returns:

             Returns the package name.

           Raises:

             passed through exceptions

getmodule_oid_sub
^^^^^^^^^^^^^^^^^
	.. autofunction:: getmodule_oid_sub
    
           Args:

             mod: Module.

           Returns:

             Returns the package name.

           Raises:

             passed through exceptions

getmodule_package_name
^^^^^^^^^^^^^^^^^^^^^^
	.. autofunction:: getmodule_package_name

           Args:

             mod: Reference to a loaded module.

           Returns:

             Returns the package name of the loaded module.

           Raises:

             passed through exceptions

getmodule_type
^^^^^^^^^^^^^^
	.. autofunction:: getmodule_type

           Args:

             mod: Reference to a loaded module.

           Returns:

             Returns the module type as defined by imp, else None.
             ::
             
             	ret:=(PY_SOURCE|PY_COMPILED|C_EXTENSION|PKG_DIRECTORY|C_BUILTIN|PY_FROZEN|None)

           Raises:

             passed through exceptions


Exceptions
----------


Resources
---------
* inspect Python2 - [inspect2]_
* inspect Python3 - [inspect3]_
* pystackinfo package; Arno-Can Uestuensoez [pystackinfo]_
* types Python2 - [types2]_
* types Python3 - [types3]_
