"""Check defaults.
"""
from __future__ import absolute_import

import unittest
import os

import pysourceinfo.PySourceInfo


#
#######################
#
class CallUnits(unittest.TestCase):

    def testCase003(self):
        import sys
        _s=sys.path[:]
        sys.path.insert(0,os.path.abspath(os.path.dirname(__file__)+os.sep+'..'))
        import PySourceInfo_check #@UnresolvedImport
        
        fpn = os.path.normpath(os.path.dirname(unittest.__file__)+os.sep+"..")
        fx = PySourceInfo_check.check_callback(pysourceinfo.PySourceInfo.getCallerModuleFilePathName,3)
        fx = pysourceinfo.PySourceInfo.getPythonPathFromSysPath(fx)
        fx = os.path.normpath(fx)


        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)

        assert fx == fpn

if __name__ == '__main__':
    unittest.main()
