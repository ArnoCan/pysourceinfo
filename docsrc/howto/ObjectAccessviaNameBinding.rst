Object Access via Name Binding
==============================

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

