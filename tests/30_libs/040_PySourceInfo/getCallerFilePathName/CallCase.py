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
        _sx = repr(sys.path)
        sys.path.insert(0,os.path.dirname(__file__)+os.sep+'..')
        import PySourceInfo_check_tests #@UnresolvedImport

        fpn = pysourceinfo.PySourceInfo.getModuleSourceFilePathName(pysourceinfo.PySourceInfo)
        fx = PySourceInfo_check_tests.check_callback(pysourceinfo.PySourceInfo.getCallerFilePathName,0)
        assert os.path.normpath(fx) == fpn
        assert _sx != repr(sys.path)
        sys.path.pop(0)
        assert _sx == repr(sys.path)

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)


    def testCase001(self):
        import sys
        _s=sys.path[:]
        _sx = repr(sys.path)
        sys.path.insert(0,os.path.dirname(__file__)+os.sep+'..')
        import PySourceInfo_check_tests #@UnresolvedImport
        
        fpn = pysourceinfo.PySourceInfo.getModuleSourceFilePathName(PySourceInfo_check_tests)
        fx = PySourceInfo_check_tests.check_callback(pysourceinfo.PySourceInfo.getCallerFilePathName,1)
        assert os.path.normpath(fx) == fpn
        assert _sx != repr(sys.path)
        sys.path.pop(0)
        assert _sx == repr(sys.path)

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)


    def testCase002(self):
        import sys
        _s=sys.path[:]
        _sx = repr(sys.path)
        sys.path.insert(0,os.path.dirname(__file__)+os.sep+'..')
        import PySourceInfo_check_tests #@UnresolvedImport
        
        fpn = os.path.abspath(os.path.normpath(__file__))
        if fpn and fpn[-3:] != '.py':
            fpn = fpn[:-3]+'py'
        fx = PySourceInfo_check_tests.check_callback(pysourceinfo.PySourceInfo.getCallerFilePathName,2)
        assert os.path.normpath(fx) == fpn
        assert _sx != repr(sys.path)
        sys.path.pop(0)
        assert _sx == repr(sys.path)

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)

    def testCase003(self):
        import sys
        _s=sys.path[:]
        _sx = repr(sys.path)
        sys.path.insert(0,os.path.dirname(__file__)+os.sep+'..')
        import PySourceInfo_check_tests #@UnresolvedImport
        
        fx = PySourceInfo_check_tests.check_callback(pysourceinfo.PySourceInfo.getCallerFilePathName,3)
        assert os.path.basename(fx) == 'case.py'
        assert _sx != repr(sys.path)
        sys.path.pop(0)
        assert _sx == repr(sys.path)

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)


if __name__ == '__main__':
    unittest.main()
