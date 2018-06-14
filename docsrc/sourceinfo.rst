Introspection - The Python RTTI and Source information
******************************************************

Blueprint
^^^^^^^^^

The features provided by the package *pysourceinfo* are
based on the standard package *inspect* with
dynamic evaluation of additional sources where required.
A flat call interface is provided for simplified application in
OO as well as simple scripting.

The provided runtime structure information on Python sources is 
covered with basically one single type of interface

.. code-block:: python
   :linenos:

    def getCaller<Interface>(spos=1):
       """ Stack position: 
          spos==0 => caller(0==CallInterface) 
          spos==1 => caller(1) 
          spos==N => caller(N==level N) 
       """
       pass

    def getModule<Interface>(spos=1):
       pass

    def getpythonpath<Interface>(spos=1):
       pass

The interface gathers the information on the defined '<Interface>' from
the call stack, loaded modules, or search path *PATH*/*PYTHONPATH*/*sys.path*.

The covered structural dynamic elements based on the call stack are:

* package

* module

* function

* class/method

* name spaces - global/local

With additional functions covering mostly static information: 

* loaded module

* sys.path - actual OID and load path

PySourceInfo - Information on Specific Object Categories
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 
Although the standard package *inspect* provides a wide variety of information 
some are still not available.
Therefore the missing is extracted by the combination of multiple sources
and rules.

In general the main sources of information are given by the
target type.

* getCaller...

    This type works on the frame stack of *inspect*
    Some data, which is not directly provided, like
    the actual used *PYTHONPATH* item, are calculated
    by combination of multiple sources.

* getModule...

    This type works on the module information mainly
    based on *__file__*, and *__name__*.

* getpythonpath...

    This type correlates *PYTHONPATH*/*sys.path* with
    provided path and file names.

The objects for which the information could be requested are
mainly categorized as follows.

* function names and file pathnames

    Provided by inspect and the module object.

* module names and file pathnames

    Provided by inspect and the module object.
 
* package names and file pathnames

    Derived from the module information including
    the global name space, and the the current content
    of *sys.path*. Thus this could be unreliable under
    some circumstances. 

Resources
^^^^^^^^^

* decorator package [msimio]_
* functools Python2 [functools2]_
* functools Python3 [functools3]_
* inspect Python2 [inspect2]_
* inspect Python3 [inspect3]_
* pystackinfo package [pystackinfo]_
* types Python2 [types2]_
* types Python3 [types3]_

