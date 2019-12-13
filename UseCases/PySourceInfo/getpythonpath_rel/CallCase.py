from __future__ import absolute_import

import unittest
import os,sys

from sourceinfo.fileinfo import getcaller_filepathname
from sourceinfo.helper import getpythonpath_rel
import testdata.pysourceinfo

#
#######################
#
class CallUnits(unittest.TestCase):

    def testcase001(self):
        _s=sys.path[:]
        sys.path.insert(0,testdata.pysourceinfo.mypath)
        import sourceinfo_check #@UnresolvedImport

        fpn = "UseCases"+os.path.sep+"PySourceInfo"+os.path.sep+"PySourceInfo_check.py"
        fx = PySourceInfo_check.check_callback(getcaller_filepathname,1)
        fx = getpythonpath_rel(fx)
        
        fpn = os.path.normpath(fpn)
        fx = os.path.normpath(fx)

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)

        assert fx == fpn

    def testcase002(self):
        import sys
        _s=sys.path[:]
        sys.path.insert(0,os.path.abspath(os.path.dirname(__file__)+os.sep+'..'))
        import sourceinfo_check #@UnresolvedImport
        
        fpn = "getpythonpath_rel/CallCase.py"
        fx = PySourceInfo_check.check_callback(getcaller_filepathname,2)

        fpn = os.path.normpath(fpn)
        fx = os.path.normpath(fx)

        fx = os.path.abspath(fx)
        fx = getpythonpath_rel(fx)
        
        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)

        assert fx == fpn or fx == fpn[:-1]

    def testcase003(self):
        import sys
        _s=sys.path[:]
        sys.path.insert(0,os.path.abspath(os.path.dirname(__file__)+os.sep+'..'))
        import sourceinfo_check #@UnresolvedImport

        fpn = "unittest/case.py"
        
        fx = PySourceInfo_check.check_callback(getcaller_filepathname,3)
        fx = getpythonpath_rel(fx)
        
        fpn = os.path.normpath(fpn)
        fx = os.path.normpath(fx)

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)

        assert fx == fpn

if __name__ == '__main__':
    unittest.main()
