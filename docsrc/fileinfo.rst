'pysourceinfo.fileinfo' - Module
********************************

The *fileinfo* modules provides information about the source location 
of callables by utilizing the *__file__* variable and the call stack.

The stack frame of inspect is in particular reduced to the common
parameter *spos*, which is the 'stack-position'
representing the level of the addressed caller.
The value *spos==0* is the function itself, whereas *spos==1* is the
first level caller. Consequently *spos==2* is the caller of the caller,
etc.

The categories of the provided information comprise:

* **packages** - Python packages.

* **modules** - Python modules - a.k.a. source files.

* **callers** - Python functions and class/object methods.

The following definition is applied:

.. note::

   A package is represented by an imported top-entity which could either be a self-contained
   module, or the *__init__.py* special module as the top-entity from a set of modules within
   a sub directory structure.

So physically a package is a distribution unit, which provides one or more 
modules. Thus the displayed result in case of packages is the module when it is a self-contained module,
the path when it is a multi-module package.

The following attributes are provided by *fileinfo*:

* name(package, module, function)

* filename

* filepathname

* item of sys.path

* relative path to item of sys.path

* line number

Dependent on the call context, some of the attribute values may
not be available.

Modules
-------

.. automodule:: pysourceinfo.fileinfo

Functions
---------

getcaller_filename
^^^^^^^^^^^^^^^^^^
	.. autofunction:: getcaller_filename

           Args:

             spos: Caller position on the stack.

           Returns:

             Returns the filename.

           Raises:

             passed through exceptions

getcaller_filepathname
^^^^^^^^^^^^^^^^^^^^^^
	.. autofunction:: getcaller_filepathname

           Args:

              spos: Caller position on the stack.

           Returns:

              Returns the file pathname.

           Raises:

              passed through exceptions

getcaller_linenumber
^^^^^^^^^^^^^^^^^^^^
   .. autofunction:: getcaller_linenumber

           Args:

             spos: Caller position on the stack.

           Returns:

             Returns the line number of the parent call.

           Raises:

             passed through exceptions

getcaller_linenumber_def
^^^^^^^^^^^^^^^^^^^^^^^^
   .. autofunction:: getcaller_linenumber_def

           Args:

             spos: Caller position on the stack.

           Returns:

             Returns the first linenumber of the calling functions/method definition.

           Raises:

             passed through exceptions

getcaller_package_filename
^^^^^^^^^^^^^^^^^^^^^^^^^^
	.. autofunction:: getcaller_package_filename
    
           Args:

             spos: Caller position on the stack.

           Returns:

             Returns the file name of the package.

           Raises:

             passed through exceptions

getcaller_package_filepathname
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	.. autofunction:: getcaller_package_filepathname
    
           Args:

             spos: Caller position on the stack.

           Returns:

             Returns the file path name of the package.

           Raises:

             passed through exceptions

getcaller_package_pathname
^^^^^^^^^^^^^^^^^^^^^^^^^^
	.. autofunction:: getcaller_package_pathname

           Relies on 'inspect'.

           Args:

             spos: Caller position on the stack.__

           Returns:

             Returns the path name to the package.

           Raises:

              passed through exceptions

getcaller_pathname
^^^^^^^^^^^^^^^^^^
	.. autofunction:: getcaller_pathname

           Args:

             spos: Caller position on the stack.

           Returns:

             Returns the filename.

           Raises:

             passed through exceptions

getcaller_pathname_rel
^^^^^^^^^^^^^^^^^^^^^^
	.. autofunction:: getcaller_pathname_rel

           Evaluates 'sys.path' first, else switches to 'inspect'.

           Args:

             spos: Caller position on the stack.

           Returns:

             Returns the path name to the package.

           Raises:

             passed through exceptions

getcaller_pathname_sub
^^^^^^^^^^^^^^^^^^^^^^
	.. autofunction:: getcaller_pathname_sub

           Evaluates 'sys.path' first, else switches to 'inspect'.

           Args:

             spos: Caller position on the stack.

           Returns:

             Returns the path name to the package.

           Raises:

             passed through exceptions

getcaller_python_pathname
^^^^^^^^^^^^^^^^^^^^^^^^^
	.. autofunction:: getcaller_python_pathname

           Args:

             spos: Caller position on the stack.

           Returns:

             Returns the name of caller module.

           Raises:

             passed through exceptions

getcaller_source_filepathname
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	.. autofunction:: getcaller_source_filepathname

           Args:

              spos: Caller position on the stack.

           Returns:

             Returns the file pathname of the source for the caller,
             else None.

           Raises:

             passed through exceptions

getmodule_filename
^^^^^^^^^^^^^^^^^^
	.. autofunction:: getmodule_filename

           Args:

             mod: Reference to a loaded module.

           Returns:

             Returns the basename of the loaded module.

           Raises:

             passed through exceptions

getmodule_filepathname
^^^^^^^^^^^^^^^^^^^^^^
	.. autofunction:: getmodule_filepathname

           Args:

             mod: Reference to a loaded module.

           Returns:

             Returns the file pathname of the loaded module.

           Raises:

             passed through exceptions

getmodule_package_pathname
^^^^^^^^^^^^^^^^^^^^^^^^^^
	.. autofunction:: getmodule_package_pathname

           Args:

             mod: Reference to a loaded module.

           Returns:

             Returns the pathname of the package.

           Raises:

             passed through exceptions

getmodule_pathname
^^^^^^^^^^^^^^^^^^
	.. autofunction:: getmodule_pathname

           Args:

             mod: Reference to a loaded module.

           Returns:

             Returns the pathname of the loaded module.

           Raises:

             passed through exceptions

getmodule_pathname_rel
^^^^^^^^^^^^^^^^^^^^^^
	.. autofunction:: getmodule_pathname_rel

           Args:

             mod: Reference to a loaded module.

           Returns:

             Returns the relative pathname of the loaded module.

           Raises:

             passed through exceptions

getmodule_pathname_sub
^^^^^^^^^^^^^^^^^^^^^^
	.. autofunction:: getmodule_pathname_sub

           Args:

             mod: Reference to a loaded module.

           Returns:

             Returns the sub pathname of the loaded module.

           Raises:

             passed through exceptions

getmodule_python_pathname
^^^^^^^^^^^^^^^^^^^^^^^^^
	.. autofunction:: getmodule_python_pathname

           Args:

             mod: Reference to a loaded module.

           Returns:

             Returns the pathname of the loaded module.

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

