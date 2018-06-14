.. raw:: html

   <div class="indextab">

Shortcuts
=========
.. toctree::
   :maxdepth: 2

   shortcuts

.. _DEVELOPMENTDOCS:

Development Documents
---------------------

* `Introspection - The Python RTTI and Source information <sourceinfo.html>`_ 
* `Name-Binding - A Python API for Files and Objects <namebinding.html>`_ 
* `Documentation of 'pysourceinfo.__init__' <pysourceinfo.html#>`_
* `Documentation of 'pysourceinfo.fileinfo' <fileinfo.html#>`_
* `Documentation of 'pysourceinfo.objectinfo' <objectinfo.html#>`_
* `Documentation of 'pysourceinfo.bininfo' <bininfo.html#>`_
* `Documentation of 'pysourceinfo.infolists' <infolists.html#>`_
* `Documentation of 'pysourceinfo.helper' <helper.html#>`_
* `API in javadoc-style <epydoc/index.html>`_

External:

* Advanced RTTI by PyStackInfo [pystackinfo]_ 


.. _DEVELOPMENTAPI:

API Shortcuts - pysourceinfo
----------------------------

See Concepts and Design of `Name-Binding - A Python API for Files and Objects <namebinding.html>`_,
overview chart for :ref:`name binding <FILENAMEBINDING>`.

.. _PYSOURCEINFO_INIT:

pysourceinfo.__init__
^^^^^^^^^^^^^^^^^^^^^
Shared constants and definitions.

+-----------------+--------------------------+
| [docs]          | [source]                 |
+=================+==========================+
| `pysourceinfo`_ | `pysourceinfo.__init__`_ |
+-----------------+--------------------------+

.. _pysourceinfo.__init__: _modules/pysourceinfo/__init__.html#
.. _pysourceinfo: pysourceinfo.html#


.. _PYSOURCEINFO_FILEINFO:

pysourceinfo.fileinfo
^^^^^^^^^^^^^^^^^^^^^

Information about Python sources files and paths
`[naming-scheme] <_images/name-binding.png>`_
`[name-binding] <namebinding.html#>`_
`[API] <fileinfo.html#>`_ `[src] <_modules/pysourceinfo/fileinfo.html#>`_

Caller
""""""

Addressed with the common parameter *spos >=0* for stack positions.

.. index::
   pair: fileinfo.caller; file
   pair: fileinfo.caller; module
   pair: fileinfo.caller; line
   pair: fileinfo.caller; path

.. _CALLERFILESANDPATHS:

+--------------------------------------------+---------------------------------------------------------+
| [docs]                                     | [source]                                                |
+============================================+=========================================================+
| `fileinfo.getcaller_filename`_             | `pysourceinfo.fileinfo.getcaller_filename`_             |
+--------------------------------------------+---------------------------------------------------------+
| `fileinfo.getcaller_filepathname`_         | `pysourceinfo.fileinfo.getcaller_filepathname`_         |
+--------------------------------------------+---------------------------------------------------------+
| `fileinfo.getcaller_linenumber`_           | `pysourceinfo.fileinfo.getcaller_linenumber`_           |
+--------------------------------------------+---------------------------------------------------------+
| `fileinfo.getcaller_linenumber_def`_       | `pysourceinfo.fileinfo.getcaller_linenumber_def`_       |
+--------------------------------------------+---------------------------------------------------------+
| `fileinfo.getcaller_package_filename`_     | `pysourceinfo.fileinfo.getcaller_package_filename`_     |
+--------------------------------------------+---------------------------------------------------------+
| `fileinfo.getcaller_package_filepathname`_ | `pysourceinfo.fileinfo.getcaller_package_filepathname`_ |
+--------------------------------------------+---------------------------------------------------------+
| `fileinfo.getcaller_package_pathname`_     | `pysourceinfo.fileinfo.getcaller_package_pathname`_     |
+--------------------------------------------+---------------------------------------------------------+
| `fileinfo.getcaller_pathname`_             | `pysourceinfo.fileinfo.getcaller_pathname`_             |
+--------------------------------------------+---------------------------------------------------------+
| `fileinfo.getcaller_pathname_rel`_         | `pysourceinfo.fileinfo.getcaller_pathname_rel`_         |
+--------------------------------------------+---------------------------------------------------------+
| `fileinfo.getcaller_pathname_sub`_         | `pysourceinfo.fileinfo.getcaller_pathname_sub`_         |
+--------------------------------------------+---------------------------------------------------------+
| `fileinfo.getcaller_python_pathname`_      | `pysourceinfo.fileinfo.getcaller_python_pathname`_      |
+--------------------------------------------+---------------------------------------------------------+

.

.. index::
   pair: fileinfo.module; file
   pair: fileinfo.module; name
   pair: fileinfo.module; package
   pair: fileinfo.module; source

.. _CallerModulesFiles:

Modules
"""""""

Addressed with the common parameter *mod* for modules objects.

+-----------------------------------------+------------------------------------------------------+
| [docs]                                  | [source]                                             |
+=========================================+======================================================+
| `fileinfo.getmodule_filename`_          | `pysourceinfo.fileinfo.getmodule_filename`_          |
+-----------------------------------------+------------------------------------------------------+
| `fileinfo.getmodule_filepathname`_      | `pysourceinfo.fileinfo.getmodule_filepathname`_      |
+-----------------------------------------+------------------------------------------------------+
| `fileinfo.getmodule_filepathname_type`_ | `pysourceinfo.fileinfo.getmodule_filepathname_type`_ |
+-----------------------------------------+------------------------------------------------------+
| `fileinfo.getmodule_package_pathname`_  | `pysourceinfo.fileinfo.getmodule_package_pathname`_  |
+-----------------------------------------+------------------------------------------------------+
| `fileinfo.getmodule_pathname`_          | `pysourceinfo.fileinfo.getmodule_pathname`_          |
+-----------------------------------------+------------------------------------------------------+
| `fileinfo.getmodule_pathname_rel`_      | `pysourceinfo.fileinfo.getmodule_pathname_rel`_      |
+-----------------------------------------+------------------------------------------------------+
| `fileinfo.getmodule_pathname_sub`_      | `pysourceinfo.fileinfo.getmodule_pathname_sub`_      |
+-----------------------------------------+------------------------------------------------------+
| `fileinfo.getmodule_python_pathname`_   | `pysourceinfo.fileinfo.getmodule_python_pathname`_   |
+-----------------------------------------+------------------------------------------------------+

.

.. _PYSOURCEINFO_OBJECTINFO:

pysourceinfo.objectinfo
^^^^^^^^^^^^^^^^^^^^^^^

Information on runtime objects
`[naming-scheme] <_images/name-binding.png>`_
`[name-binding] <namebinding.html#>`_
`[API] <objectinfo.html#>`_ `[src] <_modules/pysourceinfo/objectinfo.html#>`_


.. index::
   pair: objectinfo.caller; name
   pair: objectinfo.caller; module
   pair: objectinfo.caller; package

Caller
""""""

Addressed with the common parameter *spos >=0* for stack positions.

+--------------------------------------+---------------------------------------------------+
| [docs]                               | [source]                                          |
+======================================+===================================================+
| `objectinfo.getcaller_name`_         | `pysourceinfo.objectinfo.getcaller_name`_         |
+--------------------------------------+---------------------------------------------------+
| `objectinfo.getcaller_name_sub`_     | `pysourceinfo.objectinfo.getcaller_name_sub`_     |
+--------------------------------------+---------------------------------------------------+
| `objectinfo.getcaller_module`_       | `pysourceinfo.objectinfo.getcaller_module`_       |
+--------------------------------------+---------------------------------------------------+
| `objectinfo.getcaller_module_name`_  | `pysourceinfo.objectinfo.getcaller_module_name`_  |
+--------------------------------------+---------------------------------------------------+
| `objectinfo.getcaller_package_name`_ | `pysourceinfo.objectinfo.getcaller_package_name`_ |
+--------------------------------------+---------------------------------------------------+

.

.. index::
   pair: objectinfo.module; name
   pair: objectinfo.module; ID
   pair: objectinfo.module; package
   pair: objectinfo.module; OID
   pair: objectinfo.module; type

Modules
"""""""

+--------------------------------------+---------------------------------------------------+
| [docs]                               | [source]                                          |
+======================================+===================================================+
| `objectinfo.getmodule_by_id`_        | `pysourceinfo.objectinfo.getmodule_by_id`_        |
+--------------------------------------+---------------------------------------------------+
| `objectinfo.getmodule_by_name`_      | `pysourceinfo.objectinfo.getmodule_by_name`_      |
+--------------------------------------+---------------------------------------------------+
| `objectinfo.getmodule_name`_         | `pysourceinfo.objectinfo.getmodule_name`_         |
+--------------------------------------+---------------------------------------------------+
| `objectinfo.getmodule_name_sub`_     | `pysourceinfo.objectinfo.getmodule_name_sub`_     |
+--------------------------------------+---------------------------------------------------+
| `objectinfo.getmodule_oid`_          | `pysourceinfo.objectinfo.getmodule_oid`_          |
+--------------------------------------+---------------------------------------------------+
| `objectinfo.getmodule_oid_sub`_      | `pysourceinfo.objectinfo.getmodule_oid_sub`_      |
+--------------------------------------+---------------------------------------------------+
| `objectinfo.getmodule_type`_         | `pysourceinfo.objectinfo.getmodule_type`_         |
+--------------------------------------+---------------------------------------------------+
| `objectinfo.getmodule_package_name`_ | `pysourceinfo.objectinfo.getmodule_package_name`_ |
+--------------------------------------+---------------------------------------------------+

.

.. index::
   single: PYTHONPATH

.. _PYSOURCEINFO_INFOLISTS:

pysourceinfo.infolists
^^^^^^^^^^^^^^^^^^^^^^

Lists and items of source information for runtime components
`[naming-scheme] <_images/name-binding.png>`_
`[name-binding] <namebinding.html#>`_
`[API] <infolists.html#>`_ `[src] <_modules/pysourceinfo/infolists.html#>`_

.. index::
   pair: objectinfo.infolists; name
   pair: objectinfo.infolists; ID
   pair: objectinfo.infolists; module
   pair: objectinfo.infolists; PYTHONPATH
   pair: objectinfo.infolists; path

Modules
"""""""

Addressed with the common parameter *mod* for memory address.

+-------------------------------------------------+--------------------------------------------------------------+
| [docs]                                          | [source]                                                     |
+=================================================+==============================================================+
| `infolists.getsysmodules_id_list`_              | `pysourceinfo.infolists.getsysmodules_id_list`_              |
+-------------------------------------------------+--------------------------------------------------------------+
| `infolists.getsysmodules_list`_                 | `pysourceinfo.infolists.getsysmodules_list`_                 |
+-------------------------------------------------+--------------------------------------------------------------+
| `infolists.getsysmodules_name_list`_            | `pysourceinfo.infolists.getsysmodules_name_list`_            |
+-------------------------------------------------+--------------------------------------------------------------+
| `infolists.getsysmodules_pathname_list`_        | `pysourceinfo.infolists.getsysmodules_pathname_list`_        |
+-------------------------------------------------+--------------------------------------------------------------+
| `infolists.getsysmodules_python_pathname_list`_ | `pysourceinfo.infolists.getsysmodules_python_pathname_list`_ |
+-------------------------------------------------+--------------------------------------------------------------+
| `infolists.getsysmodules_pathname_rel_list`_    | `pysourceinfo.infolists.getsysmodules_pathname_rel_list`_    |
+-------------------------------------------------+--------------------------------------------------------------+

.. _PYSOURCEINFO_BININFO:

pysourceinfo.bininfo
^^^^^^^^^^^^^^^^^^^^

Runtime Type Information for Python sources, core functions.
`[naming-scheme] <_images/name-binding.png>`_
`[name-binding] <namebinding.html#>`_
`[API] <bininfo.html#>`_ `[src] <_modules/pysourceinfo/bininfo.html#>`_

.. index::
   pair: bininfo.caller; file
   pair: bininfo.caller; path

Caller
""""""

Addressed with the common parameter *spos >=0* for stack positions.

.. _CALLERFILESANDPATHS:

+---------------------------------------+----------------------------------------------------+
| [docs]                                | [source]                                           |
+=======================================+====================================================+
| `bininfo.getcaller_bin_filename`_     | `pysourceinfo.bininfo.getcaller_bin_filename`_     |
+---------------------------------------+----------------------------------------------------+
| `bininfo.getcaller_bin_filepathname`_ | `pysourceinfo.bininfo.getcaller_bin_filepathname`_ |
+---------------------------------------+----------------------------------------------------+
| `bininfo.getcaller_bin_pathname`_     | `pysourceinfo.bininfo.getcaller_bin_pathname`_     |
+---------------------------------------+----------------------------------------------------+
| `bininfo.getcaller_bin_pathname_rel`_ | `pysourceinfo.bininfo.getcaller_bin_pathname_rel`_ |
+---------------------------------------+----------------------------------------------------+
| `bininfo.getcaller_bin_pathname_sub`_ | `pysourceinfo.bininfo.getcaller_bin_pathname_sub`_ |
+---------------------------------------+----------------------------------------------------+

.

.. index::
   pair: bininfo.module; file
   pair: bininfo.module; name

.. _CallerModulesFiles:

Modules
"""""""

Addressed with the common parameter *mod* for modules objects.

+---------------------------------------+----------------------------------------------------+
| [docs]                                | [source]                                           |
+=======================================+====================================================+
| `bininfo.getmodule_bin_filename`_     | `pysourceinfo.bininfo.getmodule_bin_filename`_     |
+---------------------------------------+----------------------------------------------------+
| `bininfo.getmodule_bin_filepathname`_ | `pysourceinfo.bininfo.getmodule_bin_filepathname`_ |
+---------------------------------------+----------------------------------------------------+
| `bininfo.getmodule_bin_pathname`_     | `pysourceinfo.bininfo.getmodule_bin_pathname`_     |
+---------------------------------------+----------------------------------------------------+
| `bininfo.getmodule_bin_pathname_rel`_ | `pysourceinfo.bininfo.getmodule_bin_pathname_rel`_ |
+---------------------------------------+----------------------------------------------------+
| `bininfo.getmodule_bin_pathname_sub`_ | `pysourceinfo.bininfo.getmodule_bin_pathname_sub`_ |
+---------------------------------------+----------------------------------------------------+

.

.. _PYSOURCEINFO_HELPER:

pysourceinfo.helper
^^^^^^^^^^^^^^^^^^^

.. index::
   pair: pysourceinfo.helper; stack
   pair: pysourceinfo.helper; frame
   pair: pysourceinfo.helper; PYTHONPATH

Common helper 
`[naming-scheme] <_images/name-binding.png>`_
`[name-binding] <namebinding.html#>`_
`[API] <helper.html#>`_ `[src] <_modules/pysourceinfo/helper.html#>`_

+--------------------------------+---------------------------------------------+
| [docs]                         | [source]                                    |
+================================+=============================================+
| `helper.getfilepathname_type`_ | `pysourceinfo.helper.getfilepathname_type`_ |
+--------------------------------+---------------------------------------------+
| `helper.getpythonpath`_        | `pysourceinfo.helper.getpythonpath`_        |
+--------------------------------+---------------------------------------------+
| `helper.getpythonpath_rel`_    | `pysourceinfo.helper.getpythonpath_rel`_    |
+--------------------------------+---------------------------------------------+
| `helper.getstack_frame`_       | `pysourceinfo.helper.getstack_frame`_       |
+--------------------------------+---------------------------------------------+
| `helper.getstack_len`_         | `pysourceinfo.helper.getstack_len`_         |
+--------------------------------+---------------------------------------------+
| `helper.matchpath`_            | `pysourceinfo.helper.matchpath`_            |
+--------------------------------+---------------------------------------------+

.. _infolists.getsysmodules_id_list: infolists.html#pysourceinfo.infolists.getsysmodules_id_list
.. _infolists.getsysmodules_list: infolists.html#pysourceinfo.infolists.getsysmodules_list
.. _infolists.getsysmodules_name_list: infolists.html#pysourceinfo.infolists.getsysmodules_name_list
.. _infolists.getsysmodules_pathname_list: infolists.html#pysourceinfo.infolists.getsysmodules_pathname_list
.. _infolists.getsysmodules_pathname_rel_list: infolists.html#pysourceinfo.infolists.getsysmodules_pathname_rel_list
.. _infolists.getsysmodules_python_pathname_list: infolists.html#pysourceinfo.infolists.getsysmodules_python_pathname_list
.. _pysourceinfo.infolists.getsysmodules_id_list: _modules/pysourceinfo/infolists.html#getsysmodules_id_list
.. _pysourceinfo.infolists.getsysmodules_list: _modules/pysourceinfo/infolists.html#getsysmodules_list
.. _pysourceinfo.infolists.getsysmodules_name_list: _modules/pysourceinfo/infolists.html#getsysmodules_name_list
.. _pysourceinfo.infolists.getsysmodules_pathname_list: _modules/pysourceinfo/infolists.html#getsysmodules_pathname_list
.. _pysourceinfo.infolists.getsysmodules_pathname_rel_list: _modules/pysourceinfo/infolists.html#getsysmodules_pathname_rel_list
.. _pysourceinfo.infolists.getsysmodules_python_pathname_list: _modules/pysourceinfo/infolists.html#getsysmodules_python_pathname_list
.. _helper.getfilepathname_type: helper.html#pysourceinfo.helper.getfilepathname_type
.. _helper.getpythonpath: helper.html#pysourceinfo.helper.getpythonpath
.. _helper.getpythonpath_rel: helper.html#pysourceinfo.helper.getpythonpath_rel
.. _helper.getstack_frame: helper.html#pysourceinfo.helper.getstack_frame
.. _helper.getstack_len: helper.html#pysourceinfo.helper.getstack_len
.. _helper.matchpath: helper.html#pysourceinfo.helper.matchpath
.. _pysourceinfo.helper.getpythonpath: _modules/pysourceinfo/helper.html#getpythonpath
.. _pysourceinfo.helper.getpythonpath_rel: _modules/pysourceinfo/helper.html#getpythonpath_rel
.. _pysourceinfo.helper.getstack_frame: _modules/pysourceinfo/helper.html#getstack_frame
.. _pysourceinfo.helper.getstack_len: _modules/pysourceinfo/helper.html#getstack_len
.. _pysourceinfo.helper.matchpath: _modules/pysourceinfo/helper.html#matchpath
.. _pysourceinfo.helper.getfilepathname_type: _modules/pysourceinfo/helper.html#getfilepathname_type
.. _bininfo.getcaller_bin_filename: bininfo.html#pysourceinfo.bininfo.getcaller_bin_filename
.. _bininfo.getcaller_bin_filepathname: bininfo.html#pysourceinfo.bininfo.getcaller_bin_filepathname
.. _bininfo.getcaller_bin_pathname: bininfo.html#pysourceinfo.bininfo.getcaller_bin_pathname
.. _bininfo.getcaller_bin_pathname_rel: bininfo.html#pysourceinfo.bininfo.getcaller_bin_pathname_rel
.. _bininfo.getcaller_bin_pathname_sub: bininfo.html#pysourceinfo.bininfo.getcaller_bin_pathname_sub
.. _bininfo.getmodule_bin_filename: bininfo.html#pysourceinfo.bininfo.getmodule_bin_filename
.. _bininfo.getmodule_bin_filepathname: bininfo.html#pysourceinfo.bininfo.getmodule_bin_filepathname
.. _bininfo.getmodule_bin_pathname: bininfo.html#pysourceinfo.bininfo.getmodule_bin_pathname
.. _bininfo.getmodule_bin_pathname_rel: bininfo.html#pysourceinfo.bininfo.getmodule_bin_pathname_rel
.. _bininfo.getmodule_bin_pathname_sub: bininfo.html#pysourceinfo.bininfo.getmodule_bin_pathname_sub
.. _fileinfo.getcaller_filename: fileinfo.html#pysourceinfo.fileinfo.getcaller_filename
.. _fileinfo.getcaller_filepathname: fileinfo.html#pysourceinfo.fileinfo.getcaller_filepathname
.. _fileinfo.getcaller_linenumber: fileinfo.html#pysourceinfo.fileinfo.getcaller_linenumber
.. _fileinfo.getcaller_linenumber_def: fileinfo.html#pysourceinfo.fileinfo.getcaller_linenumber_def
.. _fileinfo.getcaller_package_filename: fileinfo.html#pysourceinfo.fileinfo.getcaller_package_filepathname
.. _fileinfo.getcaller_package_filepathname: fileinfo.html#pysourceinfo.fileinfo.getcaller_package_filename
.. _fileinfo.getcaller_package_pathname: fileinfo.html#pysourceinfo.fileinfo.getcaller_package_pathname
.. _fileinfo.getcaller_pathname: fileinfo.html#pysourceinfo.fileinfo.getcaller_pathname
.. _fileinfo.getcaller_pathname_rel: fileinfo.html#pysourceinfo.fileinfo.getcaller_pathname_rel
.. _fileinfo.getcaller_pathname_sub: fileinfo.html#pysourceinfo.fileinfo.getcaller_pathname_sub
.. _fileinfo.getcaller_python_pathname: fileinfo.html#pysourceinfo.fileinfo.getcaller_python_pathname
.. _fileinfo.getmodule_package_pathname: fileinfo.html#pysourceinfo.fileinfo.getmodule_package_pathname
.. _fileinfo.getmodule_pathname: fileinfo.html#pysourceinfo.fileinfo.getmodule_pathname
.. _fileinfo.getmodule_pathname_rel: fileinfo.html#pysourceinfo.fileinfo.getmodule_pathname_rel
.. _fileinfo.getmodule_pathname_sub: fileinfo.html#pysourceinfo.fileinfo.getmodule_pathname_sub
.. _fileinfo.getmodule_python_pathname: fileinfo.html#pysourceinfo.fileinfo.getmodule_python_pathname
.. _objectinfo.getmodule_type: objectinfo.html#pysourceinfo.objectinfo.getmodule_type
.. _fileinfo.getmodule_filename: fileinfo.html#pysourceinfo.fileinfo.getmodule_filename
.. _fileinfo.getmodule_filepathname: fileinfo.html#pysourceinfo.fileinfo.getmodule_filepathname
.. _fileinfo.getmodule_filepathname_type: fileinfo.html#pysourceinfo.fileinfo.getmodule_filepathname_type
.. _pysourceinfo.objectinfo.getCallerOID: _modules/pysourceinfo/objectinfo.html#getCallerOID
.. _objectinfo.getCallerOID: objectinfo.html#pysourceinfo.objectinfo.getCallerOID
.. _pysourceinfo.objectinfo.getCallerOIDSub: _modules/pysourceinfo/objectinfo.html#getCallerOIDSub
.. _objectinfo.getCallerOIDSub: objectinfo.html#pysourceinfo.objectinfo.getCallerOIDSub
.. _pysourceinfo.objectinfo.getcaller_module: _modules/pysourceinfo/objectinfo.html#getcaller_module
.. _objectinfo.getcaller_module: objectinfo.html#pysourceinfo.objectinfo.getcaller_module
.. _pysourceinfo.objectinfo.getcaller_module_name: _modules/pysourceinfo/objectinfo.html#getcaller_module_name
.. _objectinfo.getcaller_module_name: objectinfo.html#pysourceinfo.objectinfo.getcaller_module_name
.. _pysourceinfo.objectinfo.getcaller_name: _modules/pysourceinfo/objectinfo.html#getcaller_name
.. _objectinfo.getcaller_name: objectinfo.html#pysourceinfo.objectinfo.getcaller_name
.. _pysourceinfo.objectinfo.getcaller_name_sub: _modules/pysourceinfo/objectinfo.html#getcaller_name_sub
.. _objectinfo.getcaller_name_sub: objectinfo.html#pysourceinfo.objectinfo.getcaller_name_sub
.. _pysourceinfo.objectinfo.getcaller_package_name: _modules/pysourceinfo/objectinfo.html#getcaller_package_name
.. _objectinfo.getcaller_package_name: objectinfo.html#pysourceinfo.objectinfo.getcaller_package_name
.. _pysourceinfo.objectinfo.getmodule_by_id: _modules/pysourceinfo/objectinfo.html#getmodule_by_id
.. _objectinfo.getmodule_by_id: objectinfo.html#pysourceinfo.objectinfo.getmodule_by_id
.. _pysourceinfo.objectinfo.getmodule_by_name: _modules/pysourceinfo/objectinfo.html#getmodule_by_name
.. _objectinfo.getmodule_by_name: objectinfo.html#pysourceinfo.objectinfo.getmodule_by_name
.. _pysourceinfo.objectinfo.getmodule_name: _modules/pysourceinfo/objectinfo.html#getmodule_name
.. _objectinfo.getmodule_name: objectinfo.html#pysourceinfo.objectinfo.getmodule_name
.. _pysourceinfo.objectinfo.getmodule_name_sub: _modules/pysourceinfo/objectinfo.html#getmodule_name_sub
.. _objectinfo.getmodule_name_sub: objectinfo.html#pysourceinfo.objectinfo.getmodule_name_sub
.. _pysourceinfo.objectinfo.getmodule_oid: _modules/pysourceinfo/objectinfo.html#getmodule_oid
.. _objectinfo.getmodule_oid: objectinfo.html#pysourceinfo.objectinfo.getmodule_oid
.. _pysourceinfo.objectinfo.getmodule_oid_sub: _modules/pysourceinfo/objectinfo.html#getmodule_oid_sub
.. _objectinfo.getmodule_oid_sub: objectinfo.html#pysourceinfo.objectinfo.getmodule_oid_sub
.. _pysourceinfo.objectinfo.getmodule_package_name: _modules/pysourceinfo/objectinfo.html#getmodule_package_name
.. _objectinfo.getmodule_package_name: objectinfo.html#pysourceinfo.objectinfo.getmodule_package_name
.. _pysourceinfo.objectinfo.getmodule_type: _modules/pysourceinfo/objectinfo.html#getmodule_type
.. _pysourceinfo.bininfo.getcaller_bin_filename: _modules/pysourceinfo/bininfo.html#getcaller_bin_filename
.. _pysourceinfo.bininfo.getcaller_bin_filepathname: _modules/pysourceinfo/bininfo.html#getcaller_bin_filepathname
.. _pysourceinfo.bininfo.getcaller_bin_pathname: _modules/pysourceinfo/bininfo.html#getcaller_bin_pathname
.. _pysourceinfo.bininfo.getcaller_bin_pathname_rel: _modules/pysourceinfo/bininfo.html#getcaller_bin_pathname_rel
.. _pysourceinfo.bininfo.getcaller_bin_pathname_sub: _modules/pysourceinfo/bininfo.html#getcaller_bin_pathname_sub
.. _pysourceinfo.bininfo.getmodule_bin_filename: _modules/pysourceinfo/bininfo.html#getmodule_bin_filename
.. _pysourceinfo.bininfo.getmodule_bin_filepathname: _modules/pysourceinfo/bininfo.html#getmodule_bin_filepathname
.. _pysourceinfo.bininfo.getmodule_bin_pathname: _modules/pysourceinfo/bininfo.html#getmodule_bin_pathname
.. _pysourceinfo.bininfo.getmodule_bin_pathname_rel: _modules/pysourceinfo/bininfo.html#getmodule_bin_pathname_rel
.. _pysourceinfo.bininfo.getmodule_bin_pathname_sub: _modules/pysourceinfo/bininfo.html#getmodule_bin_pathname_sub
.. _pysourceinfo.fileinfo.getcaller_filename: _modules/pysourceinfo/fileinfo.html#getcaller_filename
.. _pysourceinfo.fileinfo.getcaller_filepathname: _modules/pysourceinfo/fileinfo.html#getcaller_filepathname
.. _pysourceinfo.fileinfo.getcaller_linenumber: _modules/pysourceinfo/fileinfo.html#getcaller_linenumber
.. _pysourceinfo.fileinfo.getcaller_linenumber_def: _modules/pysourceinfo/fileinfo.html#getcaller_linenumber_def
.. _pysourceinfo.fileinfo.getcaller_package_filename: _modules/pysourceinfo/fileinfo.html#getcaller_package_filename
.. _pysourceinfo.fileinfo.getcaller_package_filepathname: _modules/pysourceinfo/fileinfo.html#getcaller_package_filepathname
.. _pysourceinfo.fileinfo.getcaller_package_pathname: _modules/pysourceinfo/fileinfo.html#getcaller_package_pathname
.. _pysourceinfo.fileinfo.getcaller_pathname: _modules/pysourceinfo/fileinfo.html#getcaller_pathname
.. _pysourceinfo.fileinfo.getcaller_pathname_rel: _modules/pysourceinfo/fileinfo.html#getcaller_pathname_rel
.. _pysourceinfo.fileinfo.getcaller_pathname_sub: _modules/pysourceinfo/fileinfo.html#getcaller_pathname_sub
.. _pysourceinfo.fileinfo.getcaller_python_pathname: _modules/pysourceinfo/fileinfo.html#getcaller_python_pathname
.. _pysourceinfo.fileinfo.getmodule_filename: _modules/pysourceinfo/fileinfo.html#getmodule_filename
.. _pysourceinfo.fileinfo.getmodule_filepathname: _modules/pysourceinfo/fileinfo.html#getmodule_filepathname
.. _pysourceinfo.fileinfo.getmodule_filepathname_type: _modules/pysourceinfo/fileinfo.html#getmodule_filepathname_type
.. _pysourceinfo.fileinfo.getmodule_package_pathname: _modules/pysourceinfo/fileinfo.html#getmodule_package_pathname
.. _pysourceinfo.fileinfo.getmodule_pathname: _modules/pysourceinfo/fileinfo.html#getmodule_pathname
.. _pysourceinfo.fileinfo.getmodule_pathname_rel: _modules/pysourceinfo/fileinfo.html#getmodule_pathname_rel
.. _pysourceinfo.fileinfo.getmodule_pathname_sub: _modules/pysourceinfo/fileinfo.html#getmodule_pathname_sub
.. _pysourceinfo.fileinfo.getmodule_python_pathname: _modules/pysourceinfo/fileinfo.html#getmodule_python_pathname


HowTo - API
^^^^^^^^^^^

.. toctree::
   :maxdepth: 2

   howto

Resources
^^^^^^^^^

* inspect Python2 - [inspect2]_
* inspect Python3 - [inspect3]_
* pystackinfo package; Arno-Can Uestuensoez [pystackinfo]_
* types Python2 - [types2]_
* types Python3 - [types3]_

.. raw:: html

   </div>
