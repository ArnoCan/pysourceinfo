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

        fx0 = os.path.dirname(PySourceInfo_check_tests.__file__)
        fx1 = os.path.dirname(pysourceinfo.PySourceInfo.__file__)+os.sep+".."
        fx = PySourceInfo_check_tests.check_callback(pysourceinfo.PySourceInfo.getCallerModuleFilePathName,0)

        fx0 = os.path.abspath(fx0)
        fx1 = os.path.abspath(fx1)
        fx = os.path.abspath(fx)
        fx0 = os.path.normpath(fx0)
        fx1 = os.path.normpath(fx1)
        fx = os.path.normpath(fx)

        fx = pysourceinfo.PySourceInfo.getPythonPathFromSysPath(fx)

        assert fx == fx0 or fx == fx1

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)

    def testCase001(self):
        import sys
        _s=sys.path[:]
        sys.path.insert(0,os.path.dirname(__file__)+os.sep+'..')
        import PySourceInfo_check_tests #@UnresolvedImport

        fx0 = os.path.dirname(__file__)+os.sep+'..'
        fx1 = os.path.dirname(pysourceinfo.__file__)+os.sep+'..'
        fx = PySourceInfo_check_tests.check_callback(pysourceinfo.PySourceInfo.getCallerModuleFilePathName,1)

        fx0 = os.path.abspath(fx0)
        fx1 = os.path.abspath(fx1)
        fx = os.path.abspath(fx)
        fx0 = os.path.normpath(fx0)
        fx1 = os.path.normpath(fx1)
        fx = os.path.normpath(fx)

        fx = pysourceinfo.PySourceInfo.getPythonPathFromSysPath(fx)

        assert fx == fx0 or fx == fx1

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)


    def testCase002(self):
        import sys
        _s=sys.path[:]
        sys.path.insert(0,os.path.dirname(__file__)+os.sep+'..')
        import PySourceInfo_check_tests #@UnresolvedImport
        
        fx0 = os.path.dirname(__file__)+os.sep+'..'
        fx1 = os.path.dirname(pysourceinfo.__file__)+os.sep+'..'
        fx = PySourceInfo_check_tests.check_callback(pysourceinfo.PySourceInfo.getCallerModuleFilePathName,2)
        fx = pysourceinfo.PySourceInfo.getPythonPathFromSysPath(fx)

        fx0 = os.path.abspath(fx0)
        fx1 = os.path.abspath(fx1)
        fx = os.path.abspath(fx)
        fx0 = os.path.normpath(fx0)
        fx1 = os.path.normpath(fx1)
        fx = os.path.normpath(fx)

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)


    def testCase003(self):
        import sys
        _s=sys.path[:]
        sys.path.insert(0,os.path.dirname(__file__)+os.sep+'..')
        import PySourceInfo_check_tests #@UnresolvedImport
        
        fpn = os.path.normpath(os.path.dirname(unittest.__file__)+os.sep+"..")
        fx = PySourceInfo_check_tests.check_callback(pysourceinfo.PySourceInfo.getCallerModuleFilePathName,3)
        fx = pysourceinfo.PySourceInfo.getPythonPathFromSysPath(fx)
        fx = os.path.normpath(fx)

        assert fx == fpn

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)


if __name__ == '__main__':
    unittest.main()
