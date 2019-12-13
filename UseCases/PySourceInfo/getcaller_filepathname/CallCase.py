"""Check defaults.
"""
from __future__ import absolute_import

import unittest
import os

from sourceinfo.fileinfo import getcaller_filepathname
from sourceinfo.helper import getpythonpath
#
#######################
#
class CallUnits(unittest.TestCase):

    def testcase003(self):
        import sys
        _s=sys.path[:]
        sys.path.insert(0,os.path.abspath(os.path.dirname(__file__)+os.sep+'..'))
        import sourceinfo_check #@UnresolvedImport
        
        fpn = os.path.normpath(os.path.dirname(unittest.__file__)+os.sep+"..")

        fx = PySourceInfo_check.check_callback(getcaller_filepathname,3)
        fx = getpythonpath(fx)
        fx = os.path.normpath(fx)


        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)

        assert fx == fpn

if __name__ == '__main__':
    unittest.main()
