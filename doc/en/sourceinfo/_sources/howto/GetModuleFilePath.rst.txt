
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
