
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
