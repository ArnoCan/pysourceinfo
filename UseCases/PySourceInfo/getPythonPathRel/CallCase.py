from __future__ import absolute_import

import unittest
import os

import pysourceinfo.PySourceInfo


#
#######################
#
class CallUnits(unittest.TestCase):

    def testCase001(self):
        import sys
        _s=sys.path[:]
        sys.path.insert(0,os.path.abspath(os.path.dirname(__file__)+os.sep+'..'))
        import PySourceInfo_check #@UnresolvedImport

        fpn = "PySourceInfo_check.py"
        fx = PySourceInfo_check.check_callback(pysourceinfo.PySourceInfo.getCallerModuleFilePathName,1)
        fx = pysourceinfo.PySourceInfo.getPythonPathRel(fx)
        
        fpn = os.path.normpath(fpn)
        fx = os.path.normpath(fx)

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)

        assert fx == fpn

    def testCase002(self):
        import sys
        _s=sys.path[:]
        sys.path.insert(0,os.path.abspath(os.path.dirname(__file__)+os.sep+'..'))
        import PySourceInfo_check #@UnresolvedImport
        
        fpn = "getPythonPathRel/CallCase.py"
        fx = PySourceInfo_check.check_callback(pysourceinfo.PySourceInfo.getCallerModuleFilePathName,2)

        fpn = os.path.normpath(fpn)
        fx = os.path.normpath(fx)

        fx = os.path.abspath(fx)
        fx = pysourceinfo.PySourceInfo.getPythonPathRel(fx)
        
        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)

        assert fx == fpn

    def testCase003(self):
        import sys
        _s=sys.path[:]
        sys.path.insert(0,os.path.abspath(os.path.dirname(__file__)+os.sep+'..'))
        import PySourceInfo_check #@UnresolvedImport
        
        fpn = "unittest/case.py"
        fx = PySourceInfo_check.check_callback(pysourceinfo.PySourceInfo.getCallerModuleFilePathName,3)
        fx = pysourceinfo.PySourceInfo.getPythonPathRel(fx)
        
        fpn = os.path.normpath(fpn)
        fx = os.path.normpath(fx)

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)

        assert fx == fpn

if __name__ == '__main__':
    unittest.main()
