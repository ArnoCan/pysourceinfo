'pysourceinfo.bininfo' - Module
*******************************

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

.. automodule:: pysourceinfo.bininfo

Functions
---------

getcaller_bin_filename
^^^^^^^^^^^^^^^^^^^^^^
	.. autofunction:: getcaller_bin_filename

           Args:

             spos: Caller position on the stack.

           Returns:

             Returns the filename.

           Raises:

             passed through exceptions

getcaller_bin_filepathname
^^^^^^^^^^^^^^^^^^^^^^^^^^
	.. autofunction:: getcaller_bin_filepathname

           Args:

              spos: Caller position on the stack.

           Returns:

              Returns the file pathname.

           Raises:

              passed through exceptions

getcaller_bin_pathname
^^^^^^^^^^^^^^^^^^^^^^
	.. autofunction:: getcaller_bin_pathname

           Args:

             spos: Caller position on the stack.

           Returns:

             Returns the filename.

           Raises:

             passed through exceptions

getcaller_bin_pathname_rel
^^^^^^^^^^^^^^^^^^^^^^^^^^
	.. autofunction:: getcaller_bin_pathname_rel

           Evaluates 'sys.path' first, else switches to 'inspect'.

           Args:

             spos: Caller position on the stack.

           Returns:

             Returns the path name to the package.

           Raises:

             passed through exceptions

getcaller_bin_pathname_sub
^^^^^^^^^^^^^^^^^^^^^^^^^^
	.. autofunction:: getcaller_bin_pathname_sub

           Evaluates 'sys.path' first, else switches to 'inspect'.

           Args:

             spos: Caller position on the stack.

           Returns:

             Returns the path name to the package.

           Raises:

             passed through exceptions

getmodule_bin_filename
^^^^^^^^^^^^^^^^^^^^^^
	.. autofunction:: getmodule_bin_filename

           Args:

             mod: Reference to a loaded module.

           Returns:

             Returns the basename of the loaded module.

           Raises:

             passed through exceptions

getmodule_bin_filepathname
^^^^^^^^^^^^^^^^^^^^^^^^^^
	.. autofunction:: getmodule_bin_filepathname

           Args:

             mod: Reference to a loaded module.

           Returns:

             Returns the file pathname of the loaded module.

           Raises:

             passed through exceptions

getmodule_bin_pathname
^^^^^^^^^^^^^^^^^^^^^^
	.. autofunction:: getmodule_bin_pathname

           Args:

             mod: Reference to a loaded module.

           Returns:

             Returns the pathname of the loaded module.

           Raises:

             passed through exceptions

getmodule_bin_pathname_rel
^^^^^^^^^^^^^^^^^^^^^^^^^^
	.. autofunction:: getmodule_bin_pathname_rel

           Args:

             mod: Reference to a loaded module.

           Returns:

             Returns the relative pathname of the loaded module.

           Raises:

             passed through exceptions

getmodule_bin_pathname_sub
^^^^^^^^^^^^^^^^^^^^^^^^^^
	.. autofunction:: getmodule_bin_pathname_sub

           Args:

             mod: Reference to a loaded module.

           Returns:

             Returns the sub pathname of the loaded module.

           Raises:

             passed through exceptions

Exceptions
----------


Resources
---------
* inspect Python2 - [inspect2]_
* inspect Python3 - [inspect3]_
* types Python2 - [types2]_
* types Python3 - [types3]_
* pystackinfo package; Arno-Can Uestuensoez [pystackinfo]_

