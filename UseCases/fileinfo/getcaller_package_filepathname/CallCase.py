"""Check defaults.
"""
from __future__ import absolute_import

import unittest
import os

import pysourceinfo.fileinfo


#
#######################
#
class CallUnits(unittest.TestCase):
    def testcase000(self):
        import sys
        _sx = repr(sys.path)

        sys.path.insert(0,os.path.abspath(os.path.dirname(__file__)+os.sep+'..'))
        import fileinfo_check_usecases #@UnresolvedImport

        fpn = pysourceinfo.fileinfo.getmodule_filepathname(pysourceinfo)
        fpn =os.path.dirname(fpn)
        fx = fileinfo_check_usecases.check_callback(pysourceinfo.fileinfo.getcaller_package_filepathname,0)

        # for relative calls
        fpn =os.path.abspath(fpn)
        fx =os.path.abspath(fx)

        assert os.path.normpath(fx) == fpn
        assert _sx != repr(sys.path)
        sys.path.pop(0)
        assert _sx == repr(sys.path)

    def testcase001(self):
        import sys
        _sx = repr(sys.path)
        sys.path.insert(0,os.path.abspath(os.path.dirname(__file__)+os.sep+'..'))
        import fileinfo_check_usecases #@UnresolvedImport

        fx0 = os.path.dirname(__file__)+os.sep+'..'+os.sep+'fileinfo_check_usecases.py'
        fx1 = os.path.dirname(__file__)+os.sep+'..'+os.sep+'..'+os.sep+'__init__.py'
        fx = fileinfo_check_usecases.check_callback(pysourceinfo.fileinfo.getcaller_package_filepathname,1)

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

    def testcase002(self):
        import sys
        _sx = repr(sys.path)
        sys.path.insert(0,os.path.abspath(os.path.dirname(__file__)+os.sep+'..'))
        import fileinfo_check_usecases #@UnresolvedImport
        

        resx = os.path.normpath(os.path.dirname(__file__))
        res  = fileinfo_check_usecases.check_callback(pysourceinfo.fileinfo.getcaller_package_filepathname,2)

        assert res == resx
         
        assert _sx != repr(sys.path)
        sys.path.pop(0)
        assert _sx == repr(sys.path)

if __name__ == '__main__':
    unittest.main()
