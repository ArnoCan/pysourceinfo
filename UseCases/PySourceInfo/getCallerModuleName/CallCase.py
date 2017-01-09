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
        
        #Clear from misguided previous tests
        i=len(_s)-1
        for ix in reversed(_s):
            if ix.find('UseCases') != -1:
                sys.path.pop(i)
            i-=1

        sys.path.insert(0,os.path.abspath(os.path.dirname(__file__)+os.sep+'..'))
        import PySourceInfo_check #@UnresolvedImport

        
        fx0 = 'UseCases.PySourceInfo.getCallerModuleName.CallCase'
        fx1 = 'PySourceInfo.getCallerModuleName.CallCase'
        fx = PySourceInfo_check.check_callback(pysourceinfo.PySourceInfo.getCallerModuleName,2)

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)

        assert fx == fx0 or fx == fx1

    def testCase003(self):
        import sys
        _s=sys.path[:]

        #Clear from misguided previous tests
        i=len(_s)-1
        for ix in reversed(_s):
            if ix.find('UseCases') != -1:
                sys.path.pop(i)
            i-=1

        sys.path.insert(0,os.path.abspath(os.path.dirname(__file__)+os.sep+'..'))
        import PySourceInfo_check #@UnresolvedImport
        
        fx = PySourceInfo_check.check_callback(pysourceinfo.PySourceInfo.getCallerModuleName,3)

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)

        version = '{0}.{1}'.format(*sys.version_info[:2])
        if version == '2.6': # pragma: no cover
            assert fx == 'unittest'
        elif version == '2.7': # pragma: no cover
            assert fx == 'unittest.case'
        else:
            assert False



if __name__ == '__main__':
    unittest.main()
