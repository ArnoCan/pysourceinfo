Abstract
========

The **pysourceinfo** package provides source information on Python runtime objects
based on *inspect*, *sys*, *os*, and *imp*.
The covered objects include packages, modules, functions, methods, scripts, 
and classes by two views:

* File System View - packages, modules, and linenumbers - based on files and paths -
  :ref:`[File-Namebinding] <FILENAMEBINDING>`:
* Runtime Object View - callables, classes, and containers - based on in-memory RTTI / introspection -
  :ref:`[Object-Namebinding] <FILENAMEBINDING>`:

The supported platforms are:

* Linux, BSD, Unix, OS-X, Cygwin, and Windows
* Python2, Python3 - CPython, PyPy

Object addresses within modules - Object Identifier OID - and the display of the runtime call flow
are supported by *PyStackInfo* [pystackinfo]_.

Cockpit
=======

.. raw:: html

   <div class="markyellow">

**Prerequisite Definitions**: :ref:`NAMEBINDING`

.. raw:: html

   </div>

.. raw:: html

   <div class="indextab">

+-----------------+-----------------------------------------------+-----------------------+--------------------------------+--------------------------+
| Component       | Standards/References                          | HowTo                 | Shortcuts                      | API                      |
+=================+===============================================+=======================+================================+==========================+
| `pysourceinfo`_ |                                               |                       | :ref:`PYSOURCEINFO_INIT`       | `pysourceinfo.__init__`_ |
+-----------------+-----------------------------------------------+-----------------------+--------------------------------+--------------------------+
| `fileinfo`_     | [inspect2]_ [inspect3]_ [PEP3155]_ [PEP3147]_ | `HowTo <howto.html>`_ | :ref:`PYSOURCEINFO_FILEINFO`   | `rdbg.fileinfo`_         |
+-----------------+-----------------------------------------------+-----------------------+--------------------------------+--------------------------+
| `objectinfo`_   | [inspect2]_ [inspect3]_ [PEP3155]_ [PEP3147]_ | `HowTo <howto.html>`_ | :ref:`PYSOURCEINFO_OBJECTINFO` | `rdbg.objectinfo`_       |
+-----------------+-----------------------------------------------+-----------------------+--------------------------------+--------------------------+
| `infolists`_    |                                               | `HowTo <howto.html>`_ | :ref:`PYSOURCEINFO_INFOLISTS`  | `rdbg.infolists`_        |
+-----------------+-----------------------------------------------+-----------------------+--------------------------------+--------------------------+
| `bininfo`_      | [inspect2]_ [inspect3]_ [PEP3155]_ [PEP3147]_ | `HowTo <howto.html>`_ | :ref:`PYSOURCEINFO_BININFO`    | `rdbg.bininfo`_          |
+-----------------+-----------------------------------------------+-----------------------+--------------------------------+--------------------------+
| `helper`_       |                                               | `HowTo <howto.html>`_ | :ref:`PYSOURCEINFO_HELPER`     | `rdbg.helper`_           |
+-----------------+-----------------------------------------------+-----------------------+--------------------------------+--------------------------+

+------------------------+------------------------+
| Artifacts              | Shortcuts              |
+========================+========================+
| Concepts and Design    | :ref:`DEVELOPMENTDOCS` |
+------------------------+------------------------+
| Programming Interfaces | :ref:`DEVELOPMENTAPI`  |
+------------------------+------------------------+

.. raw:: html

   </div>

.. _pysourceinfo.__init__: _modules/pysourceinfo/__init__.html#
.. _pysourceinfo: pysourceinfo.html#

.. _Remote Debug: howto.html
.. _pyrdbg.checkrdbg.checkandremove_rdbgoptions: pyrdbg.html#checkandremove-rdbgoptions

.. _Debug Basics: howto_debug_basics.html
.. _Advance Configuration: howto_advanced_configuration.html 

.. _fileinfo: sourceinfo.html#
.. _objectinfo: sourceinfo.html#
.. _infolists: sourceinfo.html#
.. _bininfo: sourceinfo.html#
.. _helper: sourceinfo.html#

.. _rdbg.fileinfo: fileinfo.html#
.. _rdbg.objectinfo: objectinfo.html#
.. _rdbg.infolists: infolists.html#
.. _rdbg.bininfo: bininfo.html#
.. _rdbg.helper: helper.html#



Blueprint
=========

The package *PySourceInfo* provides the display of code-location for callable Python syntax 
elements including the involved class and containment hierarchy.
The name-binding as defined by the package *PySourceInfo* targets the accurate location
of static code components.
This is based on the dynamic runtime information as provided by the Python interpreter.
The *PySourceInfo* and the related *PyStackInfo* avoid 
static data preparation [PEP3155]_ and AST based approaches e.g. by [qualname]_.
In distinction pure dynamic data gathering is proceeded, which inherently provides 
also for generic code created during runtime execution.

|layerswithpystackinfoblueprint|
|layerswithpystackinfoblueprint_zoom|

.. |layerswithpystackinfoblueprint_zoom| image:: _static/zoom.png
   :alt: zoom 
   :target: _static/layers-with-pystackinfo-blueprint.png
   :width: 16

.. |layerswithpystackinfoblueprint| image:: _static/layers-with-pystackinfo-blueprint.png 
   :width: 600


The  *PySourceInfo* focuses on basic information on files, modules,
and packages, including line numbers with moderate use of the *inspect* API.
The *PyStackInfo* package focuses on advanced control flow and runtime object location,
including *decorators*, *nested classes*, and *metaclasses*.

|pysourceinfoblueprint|
|pysourceinfoblueprint_zoom|

.. |pysourceinfoblueprint_zoom| image:: _static/zoom.png
   :alt: zoom 
   :target: _static/layers-blueprint.png
   :width: 16

.. |pysourceinfoblueprint| image:: _static/layers-blueprint.png 
   :width: 450

* *objectinfo* - information about the runtime location of Python syntax elements 
* *fileinfo* - information about the source location of callables
* *bininfo* - information about the location of compiled runtime files
* *infolists* - lists and enumerations of source information
* *helper* - support functions for the PYTHONPATH and the stack access

The package *PyStackInfo* makes extended use of the stack and type information.
This provides advanced debugging and analysis in particular for typical routines
handling large data sets where the pure debugger based analysis may encounter some limits.
Both packages require the support of *inspect*, which is guaranteed in the standard CPython,
and seems to be reliably present in *PyPy*.

The provided runtime structure information on Python sources is 
covered with basically one single type of interface[`Name-Binding <namebinding.html>`_]

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

`More... <shortcuts.html>`_ 


Table of Contents
=================
.. raw:: html

   <div class="marklihoveryellow">


.. toctree::
   :maxdepth: 1

   shortcuts
   namebinding

   pysourceinfo
   bininfo
   fileinfo
   helper
   infolists
   objectinfo

   pysourceinfo.PySourceInfo

   help
   howto
   install
   todo

.. raw:: html

   </div>


Indices and tables
==================
.. raw:: html

   <div class="marklihoveryellow">

* :ref:`genindex`
* :ref:`modindex`
* `References <references.html>`_
* :ref:`search`

.. raw:: html

   </div>

Resources
=========

.. include:: project.rst

**Online Documents**

.. raw:: html

   <div class="marklihoveryellow">

* Pythonhosted: https://pythonhosted.org/pysourceinfo/

.. raw:: html

   </div>

**Licenses**

.. raw:: html

   <div class="marklihoveryellow">

* Artistic-License-2.0(base license): `ArtisticLicense20.html <_static/ArtisticLicense20.html>`_

* Forced-Fairplay-Constraints(amendments): `licenses-amendments.txt <_static/licenses-amendments.txt>`_ 

  |profileinfo|  [xkcd]_ Support the OpenSource Authors :-)

  .. |profileinfo| image:: _static/profile_info.png 
     :target: _static/profile_info.html
     :width: 48

.. raw:: html

   </div>


**Downloads**

.. raw:: html

   <div class="marklihoveryellow">

* Python Package Index: https://pypi.python.org/pypi/pysourceinfo

* Sourceforge.net: https://sourceforge.net/projects/pysourceinfo/

* github.com: https://github.com/ArnoCan/pysourceinfo/

.. raw:: html

   </div>
