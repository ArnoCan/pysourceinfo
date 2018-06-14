'pysourceinfo.infolists' - Module
*********************************

Lists and items of source information for runtime components.

Modules
-------

.. automodule:: pysourceinfo.infolists

Functions
---------

getsysmodules_filepathname_list
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	.. autofunction:: getsysmodules_filepathname_list

           Scans all modules for the packages contained in *sys.modules*.
           Args:

             r: regexpr to be applied on the file path names.

           Returns:

             Returns the list of file path names for the loaded modules.

           Raises:

             passed through exceptions

getsysmodules_id_list
^^^^^^^^^^^^^^^^^^^^^
	.. autofunction:: getsysmodules_id_list

           Args:

             r: regexpr to be applied on the IDs.

           Returns:

             Returns the list of the loaded modules.

           Raises:

             passed through exceptions

getsysmodules_list
^^^^^^^^^^^^^^^^^^
	.. autofunction:: getsysmodules_list

           Args:

             r: regexpr to be applied on the module names.

           Returns:

             Returns the list of the loaded modules.

           Raises:

             passed through exceptions

getsysmodules_name_list
^^^^^^^^^^^^^^^^^^^^^^^
	.. autofunction:: getsysmodules_name_list

           Args:

             r: regexpr to be applied on the module names.

           Returns:

             Returns the list of the names of the loaded modules.

           Raises:

             passed through exceptions

getsysmodules_pathname_list
^^^^^^^^^^^^^^^^^^^^^^^^^^^
	.. autofunction:: getsysmodules_pathname_list

           Args:

             r: regexpr to be applied on the module path names.

           Returns:

             Returns the list of pathnames of the loaded modules.

           Raises:

             passed through exceptions

getsysmodules_python_pathname_list
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	.. autofunction:: getsysmodules_python_pathname_list

           Args:

             r: regexpr to be applied on the module path names.

           Returns:

             Returns the list of pathnames of the loaded modules.

           Raises:

             passed through exceptions

getsysmodules_pathname_rel_list
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	.. autofunction:: getsysmodules_pathname_rel_list

           Args:

             r: regexpr to be applied on the module path names.

           Returns:

             Returns the list of relative pathnames of the loaded modules.

           Raises:

             passed through exceptions

Resources
---------
* inspect Python2 - [inspect2]_
* inspect Python3 - [inspect3]_
* types Python2 - [types2]_
* types Python3 - [types3]_
* pystackinfo package; Arno-Can Uestuensoez [pystackinfo]_
