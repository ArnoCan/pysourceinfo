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

        fpn = pysourceinfo.PySourceInfo.getModuleSourceFilePathName(pysourceinfo.PySourceInfo)
        
        fm = PySourceInfo_check_tests.check_callback(pysourceinfo.PySourceInfo.getCallerModule,0)
        fx = pysourceinfo.PySourceInfo.getModuleSourceFilePathName(fm)

        assert os.path.normpath(fx) == fpn
        assert fx[-3:] == '.py'

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)

    def testCase001(self):
        import sys
        _s=sys.path[:]
        sys.path.insert(0,os.path.dirname(__file__)+os.sep+'..')
        import PySourceInfo_check_tests #@UnresolvedImport
        
        fpn = pysourceinfo.PySourceInfo.getModuleSourceFilePathName(PySourceInfo_check_tests)
        
        fm = PySourceInfo_check_tests.check_callback(pysourceinfo.PySourceInfo.getCallerModule,1)
        fx = pysourceinfo.PySourceInfo.getModuleSourceFilePathName(fm)

        assert os.path.normpath(fx) == fpn
        assert fx[-3:] == '.py'

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)


    def testCase002(self):
        import sys
        _s=sys.path[:]
        sys.path.insert(0,os.path.dirname(__file__)+os.sep+'..')
        import PySourceInfo_check_tests #@UnresolvedImport
        
        fpn = os.path.normpath(__file__)
        if fpn[-4:-1] == '.py':
            fpn = fpn[:-1]
        
        fm = PySourceInfo_check_tests.check_callback(pysourceinfo.PySourceInfo.getCallerModule,2)
        fx = pysourceinfo.PySourceInfo.getModuleSourceFilePathName(fm)

        assert os.path.normpath(fx) == fpn
        assert fx[-3:] == '.py'

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)

       

    def testCase003(self):
        import sys
        _s=sys.path[:]
        sys.path.insert(0,os.path.dirname(__file__)+os.sep+'..')
        import PySourceInfo_check_tests #@UnresolvedImport
        
        fm = PySourceInfo_check_tests.check_callback(pysourceinfo.PySourceInfo.getCallerModule,3)
        fx = pysourceinfo.PySourceInfo.getModuleSourceFilePathName(fm)
        fx = os.path.basename(fx)
        
        assert os.path.basename(fx) == 'case.py'
        assert fx[-3:] == '.py'

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)


if __name__ == '__main__':
    unittest.main()