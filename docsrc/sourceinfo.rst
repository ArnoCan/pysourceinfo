
.. _PYSOURCEINFO_INIT:

sourceinfo.__init__
===================

Common definitions for the package *pysourceinfo*.

Module
------
.. automodule:: sourceinfo.__init__

Constants
---------

Search Path Resolution
^^^^^^^^^^^^^^^^^^^^^^
The resolution of the path variables for loaded modules is not
provided by the Python interpreter - at least not as a simple
usable variable.
The resolution from the *PYTHONPATH* / *sys.path* 
depends on the load mechanism, and potentially on the current
entries in the *sys.path* variable.
When loaded by a filepath this could be an arbitrary filesystem
path, or a memory block.
Due to the variety of possible load mechanisms of Python and the
lack of an interpreter variable, the implementation relies on the
*sys.path* variable by checking these as a matching path-prefix.

The *sys.path* variable could be populated with arbitrary paths
and redundancies, the python interpreter adds the startup directory
by default into the position *sys.path[0]*.
So this algorithm is by definition only as acurate,
as the current *sys.path* variable reflects the actual load-prefixes.
Therefore the *pysourceinfo* package defines constants that control
the evaluation strategy of the package path
from the search tpath list *PYTHONPATH*/*sys.path*.
In case of one matching path-prefix, this values have no effect.
The constants help for the expected resolution
in case of multiple matches, with remaining possible in-accuracies.
The controlling constants are:

* **P_FIRST**: first matched path-prefix
* **P_IGNORE0**: starts with element 1, ignores element 0
* **P_LAST**: last matched path-prefix
* **P_LONGEST**: longest matched path-prefix
* **P_SHORTEST**: longest matched path-prefix

The interfaces supporting path resolution provide the parameter
*presolve* for individual setting for each call.

The default value is stored in the package variable
with the default value *P_FIRST*.

.. code-block:: python
   :linenos:

   sourceinfo.presolve = P_FIRST


The effect of the search strategy is two-folded,

#. resolution of the path-prefix
#. resolution of relative sub-paths

The constants are consistently defining the strategy for the path-prefix only,
the resulting strategy for the sub-path resolution is therefore reziprocal.
The constants have the following effect.

* **P_FIRST**: results in arbitrary matching sub-path of the first path
* **P_LAST**: results in arbitrary matching sub-path of the last path
* **P_LONGEST**: results in shortest possible matching sub-path
* **P_SHORTEST**: results in longest possible matching sub-path

The resolution of absolute filenames of modules is not effected by the
constants.

For the shared implementation refer to `matchpath() <fileinfo.html#matchpath>`_.


File Types
^^^^^^^^^^
The following constants are defined as common and independent constants identifying
file types.
These are supported on all platforms for Python2 and Python3, where the
introduced *__pycache__* is handeled.

The values are adapted to the standard enumeration and continued consistently
over spanning the releases.

The values *MT_COMPILED_OPT1* and *MT_COMPILED_OPT2* are in the current version
partially ambiguous due to the lack of file-content analysis.

* **MT_UNKNOWN**

  .. code-block:: python
     :linenos:

     MT_UNKNOWN = 0

* **MT_SOURCE**

  .. code-block:: python
     :linenos:

     MT_SOURCE = 1  #: same value as PY_SOURCE = 1

* **MT_COMPILED**

  .. code-block:: python
     :linenos:

     MT_COMPILED = 2  #: same value as PY_COMPILED = 2

* **MT_EXTENSION**

  .. code-block:: python
     :linenos:

     MT_EXTENSION = 3  # : same value as C_EXTENSION = 3

* **MT_DIRECTORY**

  .. code-block:: python
     :linenos:

     MT_DIRECTORY = 5  # : same value as PKG_DIRECTORY = 5

* **MT_BUILTIN**

  .. code-block:: python
     :linenos:

     MT_BUILTIN = 6  # : same value as C_BUILTIN = 6

* **MT_FROZEN**

  .. code-block:: python
     :linenos:

     MT_FROZEN = 7  # : same value as PY_FROZEN = 7

* **MT_COMPILED_OPT1**

  .. code-block:: python
     :linenos:

     MT_COMPILED_OPT1 = 10  # : PY_COMPILED | <opt1> # 2 | 8

* **MT_COMPILED_OPT2**

  .. code-block:: python
     :linenos:

     MT_COMPILED_OPT2 = 18  # : PY_COMPILED | <opt2> # 2 | 16

* **MT_COMPILED_DEBUG**

  .. code-block:: python
     :linenos:

     MT_COMPILED_DEBUG = 34  # : PY_COMPILED | 0 # 2 | 32


Miscelaneous
^^^^^^^^^^^^
Shared control variables for *pysourceinfo*:

* **debug**
* **verbose**


Exceptions
----------

.. autoclass:: SourceInfoError
