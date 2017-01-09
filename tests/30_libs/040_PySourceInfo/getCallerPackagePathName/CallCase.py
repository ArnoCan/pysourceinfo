"""Check defaults.
"""
from __future__ import absolute_import

import unittest
import os

import pysourceinfo.PySourceInfo
import testdata


#
#######################
#
class CallUnits(unittest.TestCase):
    def testCase000(self):
        import sys
        _s=sys.path[:]
        sys.path.insert(0,os.path.dirname(__file__)+os.sep+'..')
        import PySourceInfo_check_tests #@UnresolvedImport

        fpn = os.path.abspath(os.path.normpath(os.path.dirname(pysourceinfo.__file__)))
#        fpn = os.path.abspath(os.path.normpath(os.path.dirname(pysourceinfo.__file__)+os.sep+".."))
        fx = PySourceInfo_check_tests.check_callback(pysourceinfo.PySourceInfo.getCallerPackagePathName,0)
        fx = os.path.normpath(fx)
        self.assertEqual(fx, fpn)

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)


    def testCase001(self):
        import sys
        _s=sys.path[:]

        fx00 = os.path.realpath(os.path.abspath(os.path.dirname(testdata.__file__)+os.sep+'..'))
        sys.path.insert(0,fx00)
        sys.path.insert(0,os.path.abspath(os.path.dirname(__file__)+os.sep+'..'))

        import PySourceInfo_check_tests #@UnresolvedImport
        fx = PySourceInfo_check_tests.check_callback(pysourceinfo.PySourceInfo.getCallerPackagePathName,2)
        fx = os.path.realpath(os.path.normpath(fx))
        fxchk = fx[len(fx00):len(fx00+os.path.sep+'tests')]
        self.assertEqual(fxchk, os.path.sep+'tests')         

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)


    def testCase002(self):
        import sys
        _s=sys.path[:]
        sys.path.insert(0,os.path.dirname(__file__)+os.sep+'..')
        import PySourceInfo_check_tests #@UnresolvedImport
        
        fx0 = os.path.dirname(PySourceInfo_check_tests.__file__)+os.sep+".."+os.sep+".."+os.sep+".."
        #fx1 = os.path.dirname(PySourceInfo_check_tests.__file__)
        fx1 = os.path.dirname(PySourceInfo_check_tests.__file__)+os.sep+".."
        fx2 = os.path.dirname(PySourceInfo_check_tests.__file__)+os.sep+".."+os.sep+".."
        fx3 = os.path.dirname(__file__)
        fx = PySourceInfo_check_tests.check_callback(pysourceinfo.PySourceInfo.getCallerPackagePathName,2)
        fx = os.path.normpath(fx)
        
        fx0 = os.path.abspath(fx0)
        fx1 = os.path.abspath(fx1)
        fx2 = os.path.abspath(fx2)
        fx3 = os.path.abspath(fx3)
        fx = os.path.abspath(fx)
        fx0 = os.path.realpath(os.path.normpath(fx0))
        fx1 = os.path.normpath(os.path.normpath(fx1))
        fx2 = os.path.normpath(os.path.normpath(fx2))
        fx3 = os.path.normpath(os.path.normpath(fx3))
        fx = os.path.normpath(os.path.normpath(fx))

        assert fx == fx0 or fx == fx1 or fx == fx2 or fx == fx3

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)


    def testCase003(self):
        import sys
        _s=sys.path[:]
        sys.path.insert(0,os.path.dirname(__file__)+os.sep+'..')
        import PySourceInfo_check_tests #@UnresolvedImport
        
        fx = PySourceInfo_check_tests.check_callback(pysourceinfo.PySourceInfo.getCallerPackagePathName,3)

        version = '{0}.{1}'.format(*sys.version_info[:2])
        if version == '2.6': # pragma: no cover
#FIXME:            self.assertEqual(os.path.basename(fx[:-1]), "unittest.py")
            self.assertEqual(os.path.basename(fx), "unittest.py")
        elif version == '2.7': # pragma: no cover
            assert os.path.basename(fx) == "unittest"
        else:
            assert False

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)


if __name__ == '__main__':
    unittest.main()
