'PySourceInfo' - RTTI for Source Code
*************************************

The package 'pysourceinfo' supports beneath the hierarchical 
navigation on filesystems, also utilities as helpers for 
source code analysis at runtime. 
This is based on the standard package 'inspect' and provides a 
flat call interface with additional correlation where required.

The provided runtime structure information on Python sources is 
covered with basically one single type of interface
  ::

    def getCaller<Interface>(spos=1):
       """ Stack position: 
          spos==0 => caller(0==CallInterface) 
          spos==1 => caller(1) 
          spos==N => caller(N==level N) 
       """
       pass

    def getModule<Interface>(spos=1):
       pass

    def getPythonPath<Interface>(spos=1):
       pass

Which gathers information on the defined '<Intefrace>' from
the call stack, loaded modules, or search path 'PYTHONPATH'/'sys.path'.

The covered structural dynamic elements based on the call stackk are:

* package

* module

* function

* class/method

* namespaces - global/local

With additional functions covering mostly static information: 

* loaded module

* sys.path - actual OID and load path

The target is to simplify the call interface of 'inspect' for the most
common calls.

A typical application is the drop-in design of regression and 
unit tests.


Information on Specific objects
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 
Although the 'inspect' package provides a wide variety of information 
some are still not available.
Therefore the missing is extracted from combination of multiple sources
and rules.

In general the main sources of information are given by the
targte type.

* getCaller...

    This type works on the frame stack of 'inspect'
    Some data, which is not directly provided, like
    the actual used PYTHONPATH item, are calculated
    by combination of multiple sources.

* getModule...

    This type works on the module information mainly
    based on '__file__', and '__name__'.

* getPythonPath...

    This type correlates PYTHONPATH/sys.path with
    provided path and file names.

The objects for which the information could be requested are
mainly categorised as follows.

* function names and filepathnames

    Provided by inspect and the module object.

* module names and filepathnames

    Provided by inspect and the module object.
 
* package names and filepathnames

    Derived from the module information including
    the global namespace, and the the current content
    of 'sys.path'. Thus this could be unreliable under
    some circumstances. 

