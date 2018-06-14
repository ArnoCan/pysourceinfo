
Howto
=====

.. toctree::
   :maxdepth: 2

   howto

Object Access via Name Binding
------------------------------

The access to the call stack at runtime combined with the cross-reference into 
the stored code and partially compiled modules requires some classification of
API groups. 
This is here divided into the file system related and logical object access
domains.
Where a clear mapping is defined by the standard Python syntax, which
is extended by the most common access Use-Cases and implemented 
with a naming-schema for all domains
:ref:`[Object-Namebinding] <OBJECTNAMEBINDING>`.

The naming schema is provided in accordance to the following API sets:
 
#. `Filesystem Binding Functions <namebinding.html#filesystem-binding-functions>`_
#. `Object Binding Functions <namebinding.html#object-binding-functions>`_
#. `Helper Functions <namebinding.html#helper-functions>`_

Thus the selection of a required interface is foreseen by the steps:

#. Define the object as source of information, e.g. the caller *Caller* from the 
   stack.
#. Select the required information, e.g. the full qualified file path name:

   .. parsed-literal::

      *fileinfo.get<obj>_filepathname*

#. Replace the *<obj>* and select the interface
   `[API] <pysourceinfo.html#getcaller_filepathname>`_:

   .. parsed-literal::

      `fileinfo.getcaller_filepathname <fileinfo.html#getcaller-filepathname>`_


Get Module File Path
--------------------
The "module file path" as in the previous example is defined as the full qualified 
pathname of the file see :ref:`[Object-Namebinding] <OBJECTNAMEBINDING>`:

.. code-block:: python
   :linenos:

   <module-file-path>

The call signature is `[Filesystem Binding Functions] <namebinding.html#filesystem-binding-functions>`_:

.. code-block:: python
   :linenos:

   get<obj>_filepathname()

Where *<obj>* is resolved to one of:

* Caller
* Frame
* Module

E.g. in case of an *Caller* by the relative stack position
`[API] <pysourceinfo.html#getcaller_filepathname>`_:

.. parsed-literal::

   `fileinfo.getmodule_filepathname <fileinfo.html#getmodule-filepathname>`_

Get PYTHONPATH Prefix
---------------------
The "PYTHONPATH Prefix" is defined as the full qualified 
directory entry from the variable *sys.path*, or similar *PYTHONPATH*.
The program may alter the *sys.path* variable, the resulting content at the time
of call is used. Thus this may eventually deviate from the expected *PYTHONPATH*
entries.

The algorithm matches the first pathname entry which could be validated as prefix
for the loaded module name.
Again, this could have been altered by the program, thus the current state of the *sys.path*
is relied on as the final anchor, even though it may eventually not accurate
:ref:`[Object-Namebinding] <OBJECTNAMEBINDING>`:

.. code-block:: python
   :linenos:

   <PYTHONPATH>

The call signature is `[Filesystem Binding Functions] <namebinding.html#filesystem-binding-functions>`_:

.. code-block:: python
   :linenos:

   get<obj>_python_pathname()

Where *<obj>* is resolved to one of:

* Caller
* Frame
* Module

E.g. in case of an *Caller* by the relative stack position
`[API] <pysourceinfo.html#getcallerpythonpath>`_:

.. parsed-literal::

   `fileinfo.getcaller_python_pathname <fileinfo.html#getmodule-python-pathname>`_

or in case of a *Module* by reference to the object
`[API] <pysourceinfo.html#getmodule_python_pathname>`_:


.. parsed-literal::

   `fileinfo.getmodule_python_pathname <fileinfo.html#getmodule-python-pathname>`_


Get Package Name
----------------
The "Package Name" is tightly coupled to the previous function related
to the *PYTHONPATH*.
The package is defined to be contained within an directory entry from
the *sys.path* variable
:ref:`[Object-Namebinding] <OBJECTNAMEBINDING>`:

.. code-block:: python
   :linenos:

   <package>

The call signature is `[Filesystem Binding Functions] <namebinding.html#filesystem-binding-functions>`_:

.. code-block:: python
   :linenos:

   get<obj>_package_filename

Where *<obj>* is resolved to one of:

* Caller
* Frame
* Module

E.g. in case of an *Caller* by the relative stack position
`[API] <pysourceinfo.html#getcallerpackage>`_:

.. parsed-literal::

   `fileinfo.getcaller_package_filename <fileinfo.html#getcaller-package-filename>`_

Get Module OID
--------------
The "Module OID" is the logical Python notation for the
:ref:`[Object-Namebinding] <OBJECTNAMEBINDING>` of a loaded Python module:

.. code-block:: python
   :linenos:

   <module-file-path-rel>

The call signature is `[Object Binding Functions] <namebinding.html#object-binding-functions>`_:

.. code-block:: python
   :linenos:

   get<obj>_module_oid()

Where *<obj>* is resolved to one of:

* Caller
* Frame
* Module

E.g. in case of a *Module* by reference to the object
`[API] <pysourceinfo.html#getmodule_oid>`_:

.. parsed-literal::

   `objectinfo.getmodule_oid <objectinfo.html#getmodule-oid>`_

Get Caller OID
--------------
The "Caller OID" is the logical Python notation for the caller name,
which is the transformed combination of the 
:ref:`[Object-Namebinding] <OBJECTNAMEBINDING>`:

.. code-block:: python
   :linenos:

   <module-file-path-rel> + <code-component(s)>

The call signature is `[Object Binding Functions] <namebinding.html#object-binding-functions>`_:

.. code-block:: python
   :linenos:

   get<obj>_module_oid()

Where *<obj>* is resolved to *Caller* for the relative stack position
`[API] <pysourceinfo.html#getCallerOID>`_:

.. parsed-literal::

   `objectinfo.getcaller_module_oid <objectinfo.html#getcaller-module-oid>`_


Get Caller Source Line Number
-----------------------------
The "Caller Source Line Number" is the line number of the definition of the caller
within the file module 
:ref:`[Object-Namebinding] <OBJECTNAMEBINDING>`:

.. code-block:: python
   :linenos:

   <module-file-path-rel> + <code-component(s)>

The call signature is `[Object Binding Functions] <namebinding.html#filesystem-binding-functions>`_:

.. code-block:: python
   :linenos:

   get<obj>_linenumber()

Where *<obj>* is resolved to *Caller* for the relative stack position
`[API] <pysourceinfo.html#getcaller_linenumber>`_:

.. parsed-literal::

   `fileinfo.getcaller_linenumber <fileinfo.html#getcaller-linenumber>`_

