API Shortcuts - pysourceinfo
============================

pysourceinfo.PySourceInfo
^^^^^^^^^^^^^^^^^^^^^^^^^
Runtime Type Information for Python sources.
`[docs] <pysourceinfo.html#>`_

* Generic

  Analysis of the the path string only.

  +---------------------------------+-------------------------------------------------+
  | [docs]                          | [source]                                        | 
  +=================================+=================================================+
  | `getPythonPathFromSysPath`_     | `PySourceInfo.getPythonPathFromSysPath`_        |
  +---------------------------------+-------------------------------------------------+
  | `getPythonPathRel`_             | `PySourceInfo.getPythonPathRel`_                |
  +---------------------------------+-------------------------------------------------+

.. _getPythonPathFromSysPath: pysourceinfo.html#pysourceinfo.PySourceInfo.getPythonPathFromSysPath
.. _PySourceInfo.getPythonPathFromSysPath: _modules/pysourceinfo/PySourceInfo.html#getPythonPathFromSysPath
.. _getPythonPathRel: pysourceinfo.html#pysourceinfo.PySourceInfo.getPythonPathRel
.. _PySourceInfo.getPythonPathRel: _modules/pysourceinfo/PySourceInfo.html#getPythonPathRel

* Callstack - Source References

  Addressed with the common parameter *spos >=0* for stack positions.

  *Priority on 'inspect'*:

  +--------------------------------------------+---------------------------------------------------------+
  | [docs]                                     | [source]                                                | 
  +============================================+=========================================================+
  | `getCallerFileName`_                       | `PySourceInfo.getCallerFileName`_                       |
  +--------------------------------------------+---------------------------------------------------------+
  | `getCallerFilePathName`_                   | `PySourceInfo.getCallerFilePathName`_                   |
  +--------------------------------------------+---------------------------------------------------------+
  | `getCallerFuncName`_                       | `PySourceInfo.getCallerFuncName`_                       |
  +--------------------------------------------+---------------------------------------------------------+
  | `getCallerLinenumber`_                     | `PySourceInfo.getCallerLinenumber`_                     |
  +--------------------------------------------+---------------------------------------------------------+
  | `getCallerModuleFilePathName`_             | `PySourceInfo.getCallerModuleFilePathName`_             |
  +--------------------------------------------+---------------------------------------------------------+
  | `getCallerModuleName`_                     | `PySourceInfo.getCallerModuleName`_                     |
  +--------------------------------------------+---------------------------------------------------------+
  | `getCallerModulePathName`_                 | `PySourceInfo.getCallerModulePathName`_                 |
  +--------------------------------------------+---------------------------------------------------------+
  | `getCallerModulePythonPath`_               | `PySourceInfo.getCallerModulePythonPath`_               |
  +--------------------------------------------+---------------------------------------------------------+
  | `getCallerName`_                           | `PySourceInfo.getCallerName`_                           |
  +--------------------------------------------+---------------------------------------------------------+
  | `getCallerNameOID`_                        | `PySourceInfo.getCallerNameOID`_                        |
  +--------------------------------------------+---------------------------------------------------------+
  | `getCallerNamespaceGlobal`_                | `PySourceInfo.getCallerNamespaceGlobal`_                |
  +--------------------------------------------+---------------------------------------------------------+
  | `getCallerNamespaceLocal`_                 | `PySourceInfo.getCallerNamespaceLocal`_                 |
  +--------------------------------------------+---------------------------------------------------------+
  | `getCallerPackageFilePathName`_            | `PySourceInfo.getCallerPackageFilePathName`_            |
  +--------------------------------------------+---------------------------------------------------------+
  | `getCallerPackageName`_                    | `PySourceInfo.getCallerPackageName`_                    |
  +--------------------------------------------+---------------------------------------------------------+
  | `getCallerPackagePathName`_                | `PySourceInfo.getCallerPackagePathName`_                |
  +--------------------------------------------+---------------------------------------------------------+
  | `getCallerPackagePythonPath`_              | `PySourceInfo.getCallerPackagePythonPath`_              |
  +--------------------------------------------+---------------------------------------------------------+
  | `getCallerPathName`_                       | `PySourceInfo.getCallerPathName`_                       |
  +--------------------------------------------+---------------------------------------------------------+


  *Priority on 'sys.path'*:

  +--------------------------------------------+---------------------------------------------------------+
  | [docs]                                     | [source]                                                | 
  +============================================+=========================================================+
  | `getCallerSysPathPackageName`_             | `PySourceInfo.getCallerSysPathPackageName`_             |
  +--------------------------------------------+---------------------------------------------------------+
  | `getCallerSysPathPackageSysPathName`_      | `PySourceInfo.getCallerSysPathPackageSysPathName`_      |
  +--------------------------------------------+---------------------------------------------------------+
  | `getCallerSysPathPackageSysPathNameRel`_   | `PySourceInfo.getCallerSysPathPackageSysPathNameRel`_   |
  +--------------------------------------------+---------------------------------------------------------+
  | `getCallerSysPathPackagePythonPath`_       | `PySourceInfo.getCallerSysPathPackagePythonPath`_       |
  +--------------------------------------------+---------------------------------------------------------+

.. _getCallerFileName: pysourceinfo.html#pysourceinfo.PySourceInfo.getCallerFileName
.. _PySourceInfo.getCallerFileName: _modules/pysourceinfo/PySourceInfo.html#getCallerFileName
.. _getCallerFilePathName: pysourceinfo.html#pysourceinfo.PySourceInfo.getCallerFilePathName
.. _PySourceInfo.getCallerFilePathName: _modules/pysourceinfo/PySourceInfo.html#getCallerFilePathName
.. _getCallerFuncName: pysourceinfo.html#pysourceinfo.PySourceInfo.getCallerFuncName
.. _PySourceInfo.getCallerFuncName: _modules/pysourceinfo/PySourceInfo.html#getCallerFuncName
.. _getCallerLinenumber: pysourceinfo.html#pysourceinfo.PySourceInfo.getCallerLinenumber
.. _PySourceInfo.getCallerLinenumber: _modules/pysourceinfo/PySourceInfo.html#getCallerLinenumber
.. _getCallerModuleFilePathName: pysourceinfo.html#pysourceinfo.PySourceInfo.getCallerModuleFilePathName
.. _PySourceInfo.getCallerModuleFilePathName: _modules/pysourceinfo/PySourceInfo.html#getCallerModuleFilePathName
.. _getCallerModuleName: pysourceinfo.html#pysourceinfo.PySourceInfo.getCallerModuleName
.. _PySourceInfo.getCallerModuleName: _modules/pysourceinfo/PySourceInfo.html#getCallerModuleName
.. _getCallerModulePathName: pysourceinfo.html#pysourceinfo.PySourceInfo.getCallerModulePathName
.. _PySourceInfo.getCallerModulePathName: _modules/pysourceinfo/PySourceInfo.html#getCallerModulePathName
.. _getCallerModulePythonPath: pysourceinfo.html#pysourceinfo.PySourceInfo.getCallerModulePythonPath
.. _PySourceInfo.getCallerModulePythonPath: _modules/pysourceinfo/PySourceInfo.html#getCallerModulePythonPath
.. _getCallerName: pysourceinfo.html#pysourceinfo.PySourceInfo.getCallerName
.. _PySourceInfo.getCallerName: _modules/pysourceinfo/PySourceInfo.html#getCallerName
.. _getCallerNameOID: pysourceinfo.html#pysourceinfo.PySourceInfo.getCallerNameOID
.. _PySourceInfo.getCallerNameOID: _modules/pysourceinfo/PySourceInfo.html#getCallerNameOID
.. _getCallerNamespaceGlobal: pysourceinfo.html#pysourceinfo.PySourceInfo.getCallerNamespaceGlobal
.. _PySourceInfo.getCallerNamespaceGlobal: _modules/pysourceinfo/PySourceInfo.html#getCallerNamespaceGlobal
.. _getCallerNamespaceLocal: pysourceinfo.html#pysourceinfo.PySourceInfo.getCallerNamespaceLocal
.. _PySourceInfo.getCallerNamespaceLocal: _modules/pysourceinfo/PySourceInfo.html#getCallerNamespaceLocal
.. _getCallerPackageFilePathName: pysourceinfo.html#pysourceinfo.PySourceInfo.getCallerPackageFilePathName
.. _PySourceInfo.getCallerPackageFilePathName: _modules/pysourceinfo/PySourceInfo.html#getCallerPackageFilePathName
.. _getCallerPackageName: pysourceinfo.html#pysourceinfo.PySourceInfo.getCallerPackageName
.. _PySourceInfo.getCallerPackageName: _modules/pysourceinfo/PySourceInfo.html#getCallerPackageName
.. _getCallerPackagePathName: pysourceinfo.html#pysourceinfo.PySourceInfo.getCallerPackagePathName
.. _PySourceInfo.getCallerPackagePathName: _modules/pysourceinfo/PySourceInfo.html#getCallerPackagePathName
.. _getCallerPackagePythonPath: pysourceinfo.html#pysourceinfo.PySourceInfo.getCallerPackagePythonPath
.. _PySourceInfo.getCallerPackagePythonPath: _modules/pysourceinfo/PySourceInfo.html#getCallerPackagePythonPath
.. _getCallerPathName: pysourceinfo.html#pysourceinfo.PySourceInfo.getCallerPathName
.. _PySourceInfo.getCallerPathName: _modules/pysourceinfo/PySourceInfo.html#getCallerPathName
.. _getCallerSysPathPackageName: pysourceinfo.html#pysourceinfo.PySourceInfo.getCallerSysPathPackageName
.. _PySourceInfo.getCallerSysPathPackageName: _modules/pysourceinfo/PySourceInfo.html#getcallersyspathpackagename
.. _getCallerSysPathPackageSysPathName: pysourceinfo.html#pysourceinfo.PySourceInfo.getCallerSysPathPackageSysPathName
.. _PySourceInfo.getCallerSysPathPackageSysPathName: _modules/pysourceinfo/PySourceInfo.html#getcallersyspathpackagesyspathname
.. _getCallerSysPathPackageSysPathNameRel: pysourceinfo.html#pysourceinfo.PySourceInfo.getCallerSysPathPackageSysPathNameRel
.. _PySourceInfo.getCallerSysPathPackageSysPathNameRel: _modules/pysourceinfo/PySourceInfo.html#getcallersyspathpackagesyspathnamerel
.. _getCallerSysPathPackagePythonPath: pysourceinfo.html#pysourceinfo.PySourceInfo.getCallerSysPathPackagePythonPath
.. _PySourceInfo.getCallerSysPathPackagePythonPath: _modules/pysourceinfo/PySourceInfo.html#getcallersyspathpackagepythonpath

..
   * Callstack - Module References

	 Addressed with the common parameter *spos >=0* for stack positions.

	 +---------------------------------+-------------------------------------------------+
	 | [docs]                          | [source]                                        | 
	 +=================================+=================================================+
	 | ...                             | ...                                             |
	 +---------------------------------+-------------------------------------------------+


* Static runtime components

  Addressed with the common parameter *mod* for memory address.

  +---------------------------------+-------------------------------------------------+
  | [docs]                          | [source]                                        | 
  +=================================+=================================================+
  | `getModuleFilePathName`_        | `PySourceInfo.getModuleFilePathName`_           |
  +---------------------------------+-------------------------------------------------+
  | `getModulePathName`_            | `PySourceInfo.getModulePathName`_               |
  +---------------------------------+-------------------------------------------------+
  | `getModuleSourceFilePathName`_  | `PySourceInfo.getModuleSourceFilePathName`_     |
  +---------------------------------+-------------------------------------------------+

.. _getModuleFilePathName: pysourceinfo.html#pysourceinfo.PySourceInfo.getModuleFilePathName
.. _PySourceInfo.getModuleFilePathName: _modules/pysourceinfo/PySourceInfo.html#getModuleFilePathName
.. _getModulePathName: pysourceinfo.html#pysourceinfo.PySourceInfo.getModulePathName
.. _PySourceInfo.getModulePathName: _modules/pysourceinfo/PySourceInfo.html#getModulePathName
.. _getModuleSourceFilePathName: pysourceinfo.html#pysourceinfo.PySourceInfo.getModuleSourceFilePathName
.. _PySourceInfo.getModuleSourceFilePathName: _modules/pysourceinfo/PySourceInfo.html#getModuleSourceFilePathName

