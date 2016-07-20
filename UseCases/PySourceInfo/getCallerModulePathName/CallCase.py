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

    def testCase002(self):
        import sys
        _s=sys.path[:]
        sys.path.insert(0,os.path.abspath(os.path.dirname(__file__)+os.sep+'..'))
        import PySourceInfo_check #@UnresolvedImport
        
        fpn = os.path.abspath(os.path.normpath(os.path.dirname(__file__)))
        fx = PySourceInfo_check.check_callback(pysourceinfo.PySourceInfo.getCallerModulePathName,2)

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)

        assert os.path.normpath(fx) == fpn

    def testCase003(self):
        import sys
        _s=sys.path[:]
        sys.path.insert(0,os.path.abspath(os.path.dirname(__file__)+os.sep+'..'))
        import PySourceInfo_check #@UnresolvedImport
        
        fx = PySourceInfo_check.check_callback(pysourceinfo.PySourceInfo.getCallerModulePathName,3)

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)

        assert os.path.basename(fx) == 'unittest'

if __name__ == '__main__':
    unittest.main()
