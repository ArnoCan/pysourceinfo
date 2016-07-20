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
        import inspect
        
        fx0 = os.path.dirname(pysourceinfo.__file__)+os.sep+'..'
        fx = PySourceInfo_check_tests.check_callback(pysourceinfo.PySourceInfo.getCallerModulePythonPath,0)

        # for relative calls
        fx0 =os.path.abspath(fx0)
        fx =os.path.abspath(fx)

        fx0 = os.path.normpath(fx0)
        fx = os.path.normpath(fx)

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)

        assert os.path.normpath(fx) == os.path.normpath(fx0)

    def testCase001(self):
        import sys
        _s=sys.path[:]
        sys.path.insert(0,os.path.dirname(__file__)+os.sep+'..')
        import PySourceInfo_check_tests #@UnresolvedImport

        #because I rely on inspect, just adapt to it's behaviour        
        fx = PySourceInfo_check_tests.check_callback(pysourceinfo.PySourceInfo.getCallerModulePythonPath,1)
        fx = os.path.normpath(fx)
        fxn = PySourceInfo_check_tests.check_callback(pysourceinfo.PySourceInfo.getCallerModuleName,1)
        if fxn == 'PySourceInfo_check_tests':
            fpn = os.path.dirname(PySourceInfo_check_tests.__file__)
            fpn = os.path.abspath(os.path.normpath(fpn))
        else:
            fpn = os.path.splitext(os.path.normpath(PySourceInfo_check_tests.__file__))[0]
            import re
            fpn = re.sub(ur"[/\\]*"+fxn+ur"[/\\]*$","",fpn)

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)

        assert fx == fpn

    def testCase002(self):
        import sys
        _s=sys.path[:]

        #Clear from misguided previous tests
        i=len(_s)-1
        for ix in reversed(_s):
            if ix.find('UseCases') != -1:
                sys.path.pop(i)
            i-=1

        sys.path.insert(0,os.path.dirname(__file__)+os.sep+'..')
        import PySourceInfo_check_tests #@UnresolvedImport
        
        fx0 = os.path.dirname(__file__)
        fx1 = os.path.dirname(PySourceInfo_check_tests.__file__)
        fx2 = os.path.dirname(PySourceInfo_check_tests.__file__)+os.sep+'..'
        fx3 = os.path.dirname(PySourceInfo_check_tests.__file__)+os.sep+'..'+os.sep+'..'
        fx4 = os.path.dirname(PySourceInfo_check_tests.__file__)+os.sep+'..'+os.sep+'..'+os.sep+'..'
        fx = PySourceInfo_check_tests.check_callback(pysourceinfo.PySourceInfo.getCallerModulePythonPath,2)
#        fx += os.sep + "tests" + os.sep + "30_libs" + os.sep + "040_PySourceInfo" + os.sep + "getCallerModulePythonPath"

        # for relative calls
        fx0 =os.path.abspath(fx0)
        fx1 =os.path.abspath(fx1)
        fx2 =os.path.abspath(fx2)
        fx3 =os.path.abspath(fx3)
        fx4 =os.path.abspath(fx4)
        fx =os.path.abspath(fx)

        fx0 = os.path.normpath(fx0)
        fx1 = os.path.normpath(fx1)
        fx2 = os.path.normpath(fx2)
        fx3 = os.path.normpath(fx3)
        fx4 = os.path.normpath(fx4)
        fx = os.path.normpath(fx)

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)

        assert fx == fx0 or fx == fx1 or fx == fx2 or fx == fx3 or fx == fx4

    def testCase003(self):
        import sys
        _s=sys.path[:]
        sys.path.insert(0,os.path.dirname(__file__)+os.sep+'..')
        import PySourceInfo_check_tests #@UnresolvedImport
        

        fpn = os.path.dirname(unittest.__file__)
        fpn = os.path.basename(fpn)
        fx = PySourceInfo_check_tests.check_callback(pysourceinfo.PySourceInfo.getCallerModulePythonPath,3)
        a = os.path.normpath(fx+os.sep+fpn)
        b = os.path.normpath(os.path.dirname(unittest.__file__))


        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)

        assert a == b 

if __name__ == '__main__':
    unittest.main()
