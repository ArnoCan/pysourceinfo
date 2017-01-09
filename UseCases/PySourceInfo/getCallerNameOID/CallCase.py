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
        _s = sys.path[:]
        _sx = repr(sys.path)
        sys.path.insert(0,os.path.abspath(os.path.dirname(__file__)+os.sep+'..'))
        import PySourceInfo_check #@UnresolvedImport
        
        fx0 = 'UseCases.PySourceInfo.getCallerNameOID.CallCase.CallUnits.testCase002'
        fx1 = 'PySourceInfo.getCallerNameOID.CallCase.CallUnits.testCase002'
        fx = PySourceInfo_check.check_callback(pysourceinfo.PySourceInfo.getCallerNameOID,2)

        assert fx == fx0 or fx == fx1
        assert _sx != repr(sys.path)
        sys.path.pop(0)
        assert _sx == repr(sys.path)

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)


    def testCase003(self):
        import sys
        _s = sys.path[:]
        _sx = repr(sys.path)
        sys.path.insert(0,os.path.abspath(os.path.dirname(__file__)+os.sep+'..'))
        import PySourceInfo_check #@UnresolvedImport
        
        fx = PySourceInfo_check.check_callback(pysourceinfo.PySourceInfo.getCallerNameOID,3)
        version = '{0}.{1}'.format(*sys.version_info[:2])
        if version == '2.6': # pragma: no cover
            assert fx == 'unittest.CallUnits.run'
        elif version == '2.7': # pragma: no cover
            assert fx == 'unittest.case.CallUnits.run'
        else:
            assert False
        
        assert _sx != repr(sys.path)
        sys.path.pop(0)
        assert _sx == repr(sys.path)

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)


if __name__ == '__main__':
    unittest.main()
