"""Check pysourceinfo.PySourceInfo.getCallerPackagePythonPath
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
        _sx = repr(sys.path)
        sys.path.insert(0,os.path.abspath(os.path.dirname(__file__)+os.sep+'..'))
        import PySourceInfo_check #@UnresolvedImport

        fx0 = os.path.normpath(os.path.dirname(__file__))
        fx1 = os.path.dirname(PySourceInfo_check.__file__)
        fx2 = os.path.dirname(PySourceInfo_check.__file__)+os.sep+'..'
        fx3 = os.path.dirname(PySourceInfo_check.__file__)+os.sep+'..'+os.sep+'..'
        fx = PySourceInfo_check.check_callback(pysourceinfo.PySourceInfo.getCallerPackagePythonPath,2)

        # for relative calls
        fx0 =os.path.abspath(fx0)
        fx1 =os.path.abspath(fx1)
        fx2 =os.path.abspath(fx2)
        fx3 =os.path.abspath(fx3)
        fx =os.path.abspath(fx)

        fx0 = os.path.normpath(fx0)
        fx1 = os.path.normpath(fx1)
        fx2 = os.path.normpath(fx2)
        fx3 = os.path.normpath(fx3)
        fx = os.path.normpath(fx)

        assert fx == fx0 or fx == fx1 or fx == fx2 or fx == fx3 
        assert _sx != repr(sys.path)
        sys.path.pop(0)
        assert _sx == repr(sys.path)

if __name__ == '__main__':
    unittest.main()
