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
    def testCase000(self):
        import sys
        _s=sys.path[:]
        sys.path.insert(0,os.path.dirname(__file__)+os.sep+'..')
        import PySourceInfo_check_tests #@UnresolvedImport

        fpn = pysourceinfo.PySourceInfo.getModulePathName(pysourceinfo.PySourceInfo)
        fx = PySourceInfo_check_tests.check_callback(pysourceinfo.PySourceInfo.getCallerPathName,0)
        assert os.path.normpath(fx) == fpn

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)


    def testCase001(self):
        import sys
        _s=sys.path[:]
        sys.path.insert(0,os.path.dirname(__file__)+os.sep+'..')
        import PySourceInfo_check_tests #@UnresolvedImport
        
        fx0 = pysourceinfo.PySourceInfo.getModulePathName(PySourceInfo_check_tests)
        fx1 = pysourceinfo.PySourceInfo.getModulePathName(pysourceinfo)
#         fx0 = PySourceInfo_check_tests.__name__
#         fx1 = "tests"
#         
#         fx = PySourceInfo_check_tests.check_callback(pysourceinfo.PySourceInfo.getCallerPackageName,1)
#         
#         # due to PyUnit path resolution dependent on curdir
#         assert fx == fx0 or fx == fx1

        fx = PySourceInfo_check_tests.check_callback(pysourceinfo.PySourceInfo.getCallerPathName,1)
        fx = os.path.normpath(fx)
        assert fx == fx0 or fx == fx1 

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)


    def testCase002(self):
        import sys
        _s=sys.path[:]
        sys.path.insert(0,os.path.dirname(__file__)+os.sep+'..')
        import PySourceInfo_check_tests #@UnresolvedImport
        
        fpn = os.path.abspath(os.path.normpath(os.path.dirname(__file__)))
        
        fx = PySourceInfo_check_tests.check_callback(pysourceinfo.PySourceInfo.getCallerPathName,2)
        fx = os.path.normpath(fx)
        assert fx == fpn

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)


    def testCase003(self):
        import sys
        _s=sys.path[:]
        sys.path.insert(0,os.path.dirname(__file__)+os.sep+'..')
        import PySourceInfo_check_tests #@UnresolvedImport
        
        fx = PySourceInfo_check_tests.check_callback(pysourceinfo.PySourceInfo.getCallerPathName,3)
        assert os.path.basename(fx) == 'unittest'

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)


if __name__ == '__main__':
    unittest.main()
