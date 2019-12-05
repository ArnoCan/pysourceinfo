
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
:ref:`[API] <def_getmodule_python_pathname>`:

.. parsed-literal::

   `fileinfo.getcaller_python_pathname <fileinfo.html#getmodule-python-pathname>`_

or in case of a *Module* by reference to the object
:ref:`[API] <def_getmodule_python_pathname>`:


.. parsed-literal::

   `fileinfo.getmodule_python_pathname <fileinfo.html#getmodule-python-pathname>`_

