"""Check defaults.
"""
from __future__ import absolute_import

import unittest
import os

import sourceinfo.objectinfo


#
#######################
#
class CallUnits(unittest.TestCase):

    def testcase002(self):
        import sys
        _s=sys.path[:]
        
        #Clear from misguided previous tests
        i=len(_s)-1
        for ix in reversed(_s):
            if ix.find('UseCases') != -1:
                sys.path.pop(i)
            i-=1

        sys.path.insert(0,os.path.abspath(os.path.dirname(__file__)+os.sep+'..'))
        import sourceinfo_check #@UnresolvedImport

        
        fx0 = 'UseCases.objectinfo.getcaller_module_name.CallCase'
        fx1 = 'objectinfo.getcaller_module_name.CallCase'
        fx = SourceInfo_check.check_callback(sourceinfo.objectinfo.getcaller_module_name,2)

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)

        assert fx == fx0 or fx == fx1

    def testcase003(self):
        import sys
        _s=sys.path[:]

        #Clear from misguided previous tests
        i=len(_s)-1
        for ix in reversed(_s):
            if ix.find('UseCases') != -1:
                sys.path.pop(i)
            i-=1

        sys.path.insert(0,os.path.abspath(os.path.dirname(__file__)+os.sep+'..'))
        import sourceinfo_check #@UnresolvedImport
        
        fx = SourceInfo_check.check_callback(sourceinfo.objectinfo.getcaller_module_name,3)

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)

        assert fx == 'unittest.case'


if __name__ == '__main__':
    unittest.main()
