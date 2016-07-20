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

        fpn = pysourceinfo.PySourceInfo.getModuleSourceFilePathName(pysourceinfo)
        fx = PySourceInfo_check_tests.check_callback(pysourceinfo.PySourceInfo.getCallerPackageFilePathName,0)

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

        fx0 = os.path.abspath(os.path.normpath(PySourceInfo_check_tests.__file__))
        if fx0[-4:-1] == '.py':
            fx0 = fx0[:-1]

        fx1 = os.path.abspath(os.path.normpath(os.path.dirname(__file__)+os.sep+'..'+os.sep+'..'+os.sep+'..'+os.sep+'__init__.py'))
        fx = PySourceInfo_check_tests.check_callback(pysourceinfo.PySourceInfo.getCallerPackageFilePathName,1)
        fx = os.path.normpath(fx)
        
        assert fx == fx0 or fx == fx1
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
        
        fx0 = os.path.dirname(__file__)+os.sep+'..'+os.sep+'__init__.py'
        fx1 = os.path.dirname(__file__)+os.sep+'..'+os.sep+'..'+os.sep+'__init__.py'
        fx2 = os.path.dirname(__file__)+os.sep+'..'+os.sep+'..'+os.sep+'..'+os.sep+'__init__.py'
        
        fx = PySourceInfo_check_tests.check_callback(pysourceinfo.PySourceInfo.getCallerPackageFilePathName,2)

        # for relative calls
        fx0 =os.path.abspath(fx0)
        fx1 =os.path.abspath(fx1)
        fx2 =os.path.abspath(fx2)
        fx =os.path.abspath(fx)

        fx0 = os.path.normpath(fx0)
        fx1 = os.path.normpath(fx1)
        fx2 = os.path.normpath(fx2)
        fx = os.path.normpath(fx)
        
        assert fx == fx0 or fx == fx1 or fx == fx2
        
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
        import re
        
        fx = PySourceInfo_check_tests.check_callback(pysourceinfo.PySourceInfo.getCallerPackageFilePathName,3)
        fx= os.path.normpath(fx)
        fx = re.sub(ur".*([/\\]unittest[/\\]__init__.py)",r'\1',fx)

        assert fx == os.sep+"unittest"+os.sep+"__init__.py"
        assert _sx != repr(sys.path)
        sys.path.pop(0)
        assert _sx == repr(sys.path)

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)


if __name__ == '__main__':
    unittest.main()
