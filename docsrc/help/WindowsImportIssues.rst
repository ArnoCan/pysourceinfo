
Windows Import Issues
=====================

**Remark**: On Windows platforms it seems to be required that the inspect module is
initialized, so for now it is required to include the following code::

   # For now a dummy call for initialization, will be cleared soon...
   import inspect
   _dummyInit = inspect.stack()

   # For example...
   from sourceinfo.PySourceInfo import getcaller_module,getcaller_name


