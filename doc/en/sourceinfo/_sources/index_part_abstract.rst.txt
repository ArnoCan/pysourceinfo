
********
Abstract
********

The **pysourceinfo** package provides source information on Python runtime objects
based on *inspect*, *sys*, *os*, and *imp*.
The covered objects include packages, modules, functions, methods, scripts, 
and classes by two views:

* File System View - packages, modules, and linenumbers - based on files and paths -
  :ref:`[File-Namebinding] <FILENAMEBINDING>`:
* Runtime Object View - callables, classes, and containers - based on in-memory RTTI / introspection -
  :ref:`[Object-Namebinding] <FILENAMEBINDING>`:

Object addresses within modules - Object Identifier OID - and the display of the runtime call flow
are supported by *PyStackInfo* [pystackinfo]_.

.. figure:: _static/layers-with-pystackinfo-blueprint.png
   :figwidth: 550
   :align: center
   :target: _static/layers-with-pystackinfo-blueprint.png
   
   Figure: Callstack Information |figuresystemabstractprint_zoom| :ref:`more... <REFERENCE_ARCHITECTURE>`

.. |figuresystemabstractprint_zoom| image:: _static/zoom.png
   :alt: zoom 
   :target: _static/layers-with-pystackinfo-blueprint.png
   :width: 16

