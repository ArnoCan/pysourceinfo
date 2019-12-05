
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

