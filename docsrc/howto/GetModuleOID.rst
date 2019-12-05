
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
