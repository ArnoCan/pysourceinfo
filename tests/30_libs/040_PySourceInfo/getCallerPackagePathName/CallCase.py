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

        fpn = os.path.abspath(os.path.normpath(os.path.dirname(pysourceinfo.__file__)+os.sep+".."))
        fx = PySourceInfo_check_tests.check_callback(pysourceinfo.PySourceInfo.getCallerPackagePathName,0)
        fx = os.path.normpath(fx)
        assert fx == fpn

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)


    def testCase001(self):
        import sys
        _s=sys.path[:]
        sys.path.insert(0,os.path.dirname(__file__)+os.sep+'..')
        import PySourceInfo_check_tests #@UnresolvedImport

        fx0 = os.path.abspath(os.path.normpath(os.path.dirname(PySourceInfo_check_tests.__file__)))
        fx1 = os.path.abspath(os.path.normpath(os.path.dirname(pysourceinfo.__file__)+os.sep+'..'))
        
        fx = PySourceInfo_check_tests.check_callback(pysourceinfo.PySourceInfo.getCallerPackagePathName,1)
        fx = os.path.normpath(fx)
        
        assert fx == fx1 or fx == fx0 

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)


    def testCase002(self):
        import sys
        _s=sys.path[:]
        sys.path.insert(0,os.path.dirname(__file__)+os.sep+'..')
        import PySourceInfo_check_tests #@UnresolvedImport
        
        fx0 = os.path.dirname(PySourceInfo_check_tests.__file__)+os.sep+".."+os.sep+".."+os.sep+".."
        #fx1 = os.path.dirname(PySourceInfo_check_tests.__file__)
        fx1 = os.path.dirname(PySourceInfo_check_tests.__file__)+os.sep+".."
        fx2 = os.path.dirname(PySourceInfo_check_tests.__file__)+os.sep+".."+os.sep+".."
        fx = PySourceInfo_check_tests.check_callback(pysourceinfo.PySourceInfo.getCallerPackagePathName,2)
        fx = os.path.normpath(fx)
        
        fx0 = os.path.abspath(fx0)
        fx1 = os.path.abspath(fx1)
        fx2 = os.path.abspath(fx2)
        fx = os.path.abspath(fx)
        fx0 = os.path.normpath(fx0)
        fx1 = os.path.normpath(fx1)
        fx2 = os.path.normpath(fx2)
        fx = os.path.normpath(fx)

        assert fx == fx0 or fx == fx1 or fx == fx2

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)


    def testCase003(self):
        import sys
        _s=sys.path[:]
        sys.path.insert(0,os.path.dirname(__file__)+os.sep+'..')
        import PySourceInfo_check_tests #@UnresolvedImport
        
        fx = PySourceInfo_check_tests.check_callback(pysourceinfo.PySourceInfo.getCallerPackagePathName,3)

        assert os.path.basename(fx) == "unittest"

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)


if __name__ == '__main__':
    unittest.main()
