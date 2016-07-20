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

        fpn = os.path.abspath(os.path.normpath(os.path.dirname(pysourceinfo.__file__)+os.sep+".."))
        fx = PySourceInfo_check_tests.check_callback(pysourceinfo.PySourceInfo.getCallerPackagePythonPath,0)
        fx = os.path.normpath(fx)
        assert fx == fpn
        assert _sx != repr(sys.path)
        sys.path.pop(0)
        assert _sx == repr(sys.path)

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)


    def testCase001(self):
        import sys
        _s=sys.path[:]
        _sx = repr(sys.path)
        sys.path.insert(0,os.path.normpath(os.path.dirname(__file__)+os.sep+'..'))
        sys.path.insert(0,os.path.normpath(os.path.dirname(__file__)))
        import PySourceInfo_check_tests #@UnresolvedImport

        fpn0 = os.path.abspath(os.path.normpath(os.path.dirname(__file__)+os.sep+'..'))
        fpn = os.path.abspath(os.path.normpath(os.path.dirname(PySourceInfo_check_tests.__file__)))

        self.assertEqual(fpn0, fpn)
        
        fx = PySourceInfo_check_tests.check_callback(pysourceinfo.PySourceInfo.getCallerPackagePythonPath,1)
        assert fx is not None

        fx = os.path.normpath(fx)
        
        fx1 = pysourceinfo.PySourceInfo.getPythonPathFromSysPath(PySourceInfo_check_tests.__file__)
        assert fx1 is not None

        fx1 = os.path.normpath(fx1)

        # REMARK: currently due to behaviour of PyUnit in conjunction with os.path.curdir
        assert fx == fpn or fx1 == fpn 

        assert _sx != repr(sys.path)
        sys.path.pop(0)
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
        
        fx0 = os.path.dirname(PySourceInfo_check_tests.__file__)+os.sep+".."+os.sep+".."+os.sep+".."
        fx1 = os.path.dirname(PySourceInfo_check_tests.__file__)+os.sep+".."+os.sep+".."
        fx2 = os.path.dirname(pysourceinfo.__file__)+os.sep+".."
        fx = PySourceInfo_check_tests.check_callback(pysourceinfo.PySourceInfo.getCallerPackagePythonPath,2)

        fx0 = os.path.abspath(fx0)
        fx1 = os.path.abspath(fx1)
        fx2 = os.path.abspath(fx2)
        fx = os.path.abspath(fx)
        fx0 = os.path.normpath(fx0)
        fx1 = os.path.normpath(fx1)
        fx2 = os.path.normpath(fx2)
        fx = os.path.normpath(fx)
        
        assert fx == fx0 or fx == fx1
        
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
        
        fpn = os.path.normpath(os.path.dirname(unittest.__file__)+os.sep+"..")
        fx = PySourceInfo_check_tests.check_callback(pysourceinfo.PySourceInfo.getCallerPackagePythonPath,3)

        assert os.path.normpath(fx) == fpn
        assert _sx != repr(sys.path)
        sys.path.pop(0)
        assert _sx == repr(sys.path)

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)


if __name__ == '__main__':
    unittest.main()
