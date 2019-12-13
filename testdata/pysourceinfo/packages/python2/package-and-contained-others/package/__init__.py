"""
Common test data for Use-Cases
==============================
Common data for 'UseCases' and 'tests'. 

* *testdata.pysourceinfo.a*: directory tree for filesystem tests
* *testdata.pysourceinfo.moduletypes*: various types for load tests
* *cro*: Call Resolution Order - Extended MRO including the dropped intermediate inheritance dependencies.
* *mro*: Standard MRO

"""

import os
mypathname = os.path.normpath(os.path.abspath(os.path.dirname(__file__)))
"""Reference path into test data. """

mypath = os.path.dirname(mypathname)
"""Search path for testdata.pysourceinfo within *PYTHONPATH*, *sys.path*."""
