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
        _sx = repr(sys.path)

        sys.path.insert(0,os.path.abspath(os.path.dirname(__file__)+os.sep+'..'))
        import PySourceInfo_check #@UnresolvedImport

        fpn = pysourceinfo.PySourceInfo.getModuleSourceFilePathName(pysourceinfo)
        fx = PySourceInfo_check.check_callback(pysourceinfo.PySourceInfo.getCallerPackageFilePathName,0)

        # for relative calls
        fpn =os.path.abspath(fpn)
        fx =os.path.abspath(fx)

        assert os.path.normpath(fx) == fpn
        assert _sx != repr(sys.path)
        sys.path.pop(0)
        assert _sx == repr(sys.path)

    def testCase001(self):
        import sys
        _sx = repr(sys.path)
        sys.path.insert(0,os.path.abspath(os.path.dirname(__file__)+os.sep+'..'))
        import PySourceInfo_check #@UnresolvedImport

        fx0 = os.path.dirname(__file__)+os.sep+'..'+os.sep+'PySourceInfo_check.py'
        fx1 = os.path.dirname(__file__)+os.sep+'..'+os.sep+'..'+os.sep+'__init__.py'
        fx = PySourceInfo_check.check_callback(pysourceinfo.PySourceInfo.getCallerPackageFilePathName,1)

        # for relative calls
        fx0 =os.path.abspath(fx0)
        fx1 =os.path.abspath(fx1)
        fx =os.path.abspath(fx)

        fx0 = os.path.normpath(fx0)
        fx1 = os.path.normpath(fx1)
        fx = os.path.normpath(fx)
        
        assert fx == fx0 or fx == fx1
        assert _sx != repr(sys.path)
        sys.path.pop(0)
        assert _sx == repr(sys.path)

    def testCase002(self):
        import sys
        _sx = repr(sys.path)
        sys.path.insert(0,os.path.abspath(os.path.dirname(__file__)+os.sep+'..'))
        import PySourceInfo_check #@UnresolvedImport
        
        fx0  = os.path.normpath(os.path.dirname(__file__)+os.sep+'..'+os.sep+'..'+os.sep+'__init__.py')
        fx1  = os.path.normpath(os.path.dirname(__file__)+os.sep+'..'+os.sep+'__init__.py')
        fx = PySourceInfo_check.check_callback(pysourceinfo.PySourceInfo.getCallerPackageFilePathName,2)
        
        # for relative calls
        fx0 =os.path.abspath(fx0)
        fx1 =os.path.abspath(fx1)
        fx =os.path.abspath(fx)

        fx0 = os.path.normpath(fx0)
        fx1 = os.path.normpath(fx1)
        fx = os.path.normpath(fx)

        assert fx == fx0 or fx == fx1
         
        assert _sx != repr(sys.path)
        sys.path.pop(0)
        assert _sx == repr(sys.path)

if __name__ == '__main__':
    unittest.main()
