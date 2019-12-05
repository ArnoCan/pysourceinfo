
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

