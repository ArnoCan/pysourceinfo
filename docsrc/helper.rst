'pysourceinfo.helper' - Module
******************************

.. automodule:: pysourceinfo.helper

Functions
---------

getfilepathname_type
^^^^^^^^^^^^^^^^^^^^
	.. autofunction:: getfilepathname_type

           Args:

           Returns:

             Returns the type of the file.

           Raises:

             passed through exceptions

getpythonpath
^^^^^^^^^^^^^
	.. autofunction:: getpythonpath

           Foreseen to be used for canonical base references in unit tests.
           This enables in particular for generic tests of filesystem positions
           where originally absolute pathnames were required.

           Args:

             pname: Pathname.

             plist: List of possible python paths.

               default := sys.path

             **kw:

               presolve: 
                  Defines the path resolution
                  strategy:

                  .. code-block:: python
                     :linenos:

                     presolve := (P_FIRST|P_LAST|P_SHORTEST|P_LONGEST) 

                  The default is stored in: 

                  .. code-block:: python
                     :linenos:

                     pysourceinfo.presolve = P_FIRST

           Returns:

             Returns the first matching path prefix from sys.path,
             as 'normpath'.

           Raises:

             passed through exceptions

getpythonpath_rel
^^^^^^^^^^^^^^^^^
	.. autofunction:: getpythonpath_rel

           REMARK: Refer also to 'getcaller_nameSpceGlobal'.

           Args:

             fpname: The file pathname.

             plist: List of possible python paths.

                default := sys.path

           Returns:

             Returns the path postfix for fpname when found,
             else 'None'.

           Raises:

             passed through exceptions

getstack_frame
^^^^^^^^^^^^^^
	.. autofunction:: getstack_frame

           Args:

           Returns:

             Returns the specified frame.

           Raises:

             passed through exceptions

getstack_len
^^^^^^^^^^^^
	.. autofunction:: getstack_len

           Args:

           Returns:

             Returns the length of current stack.

           Raises:

             passed through exceptions

matchpath
^^^^^^^^^
   .. autofunction:: matchpath

           Args:

             path:
               Path to be searched in *pathlist*.

             pathlist:
               Search path for a given *path*.

               default := *sys.path*

             pmatch:
               Match criteria for search. ::

                  pmatch := (
                     P_FIRST, P_LAST, P_SHORTEST,
                     P_LONGEST, P_IGNORE0
                  )

               default := *P_FIRST*

           Returns:

             Returns the matched pathname from pathlist.

           Raises:

             passed through exceptions

