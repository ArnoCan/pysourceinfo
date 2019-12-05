
.. _PYSOURCEINFO_FILEINFO:

sourceinfo.fileinfo
*******************

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

.. automodule:: sourceinfo.fileinfo

Functions
---------

.. _def_getcaller_filename:

getcaller_filename
^^^^^^^^^^^^^^^^^^
.. autofunction:: getcaller_filename

.. _def_getcaller_filepathname:

getcaller_filepathname
^^^^^^^^^^^^^^^^^^^^^^
.. autofunction:: getcaller_filepathname

.. _def_getcaller_linenumber:

getcaller_linenumber
^^^^^^^^^^^^^^^^^^^^
.. autofunction:: getcaller_linenumber

.. _def_getcaller_linenumber_def:

getcaller_linenumber_def
^^^^^^^^^^^^^^^^^^^^^^^^
.. autofunction:: getcaller_linenumber_def

.. _def_getcaller_package_filename:

getcaller_package_filename
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. autofunction:: getcaller_package_filename
    
.. _def_getcaller_package_filepathname:

getcaller_package_filepathname
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. autofunction:: getcaller_package_filepathname
    
.. _def_getcaller_package_pathname:

getcaller_package_pathname
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. autofunction:: getcaller_package_pathname

.. _def_getcaller_pathname:

getcaller_pathname
^^^^^^^^^^^^^^^^^^
.. autofunction:: getcaller_pathname

.. _def_getcaller_pathname_rel:

getcaller_pathname_rel
^^^^^^^^^^^^^^^^^^^^^^
.. autofunction:: getcaller_pathname_rel

.. _def_getcaller_pathname_sub:

getcaller_pathname_sub
^^^^^^^^^^^^^^^^^^^^^^
.. autofunction:: getcaller_pathname_sub

.. _def_getcaller_python_pathname:

getcaller_python_pathname
^^^^^^^^^^^^^^^^^^^^^^^^^
.. autofunction:: getcaller_python_pathname

.. _def_getcaller_source_filepathname:

getcaller_source_filepathname
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. autofunction:: getcaller_source_filepathname

.. _def_getmodule_filename:

getmodule_filename
^^^^^^^^^^^^^^^^^^
.. autofunction:: getmodule_filename

.. _def_getmodule_filepathname:

getmodule_filepathname
^^^^^^^^^^^^^^^^^^^^^^
.. autofunction:: getmodule_filepathname

.. _def_getmodule_package_pathname:

getmodule_package_pathname
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. autofunction:: getmodule_package_pathname


.. _def_getmodule_pathname:

getmodule_pathname
^^^^^^^^^^^^^^^^^^
.. autofunction:: getmodule_pathname

.. _def_getmodule_pathname_rel:

getmodule_pathname_rel
^^^^^^^^^^^^^^^^^^^^^^
.. autofunction:: getmodule_pathname_rel

.. _def_getmodule_pathname_sub:

getmodule_pathname_sub
^^^^^^^^^^^^^^^^^^^^^^
.. autofunction:: getmodule_pathname_sub

.. _def_getmodule_python_pathname:

getmodule_python_pathname
^^^^^^^^^^^^^^^^^^^^^^^^^
.. autofunction:: getmodule_python_pathname


Exceptions
----------


Resources
---------
* inspect Python2 - [inspect2]_
* inspect Python3 - [inspect3]_
* types Python2 - [types2]_
* types Python3 - [types3]_
* pystackinfo package; Arno-Can Uestuensoez [pystackinfo]_

