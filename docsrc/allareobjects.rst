
.. _ANYTHINGISANOBJECT:

Anything is an Object
=====================

Pyhton is designed around objects as the common representation for any provided
data type and callable code - in-memory as well as stored packages and modules.
Though the old implementation defines anything as an *instance*, the new implementation
is based on the common base class *object*.

The interfaces from the standard libraries provide an interface, which is 
in parts logically fragmented and requires for the RTTI queries and evaluation
some considerable knowhow and/or effort.
This is in particular the case for the mapping of stack elements and memory objects 
and onto stored files and data types.

The *PyStackInfo* provides a unified interface to handle specific tasks for
error analysis of runtime objects via a comprising seamless API.
The design is also foreseen to be applied from command line interface within
the Python interpreter, in particular via iPython.

 
E.g. the function:
::::::::::::::::::

   getObjectType()

provides a common interface with predefined enums for the RTTI of each standard type,
see `In-Memory-Objects <PyStackInfo.html#in-memory-objects>`_ .  
