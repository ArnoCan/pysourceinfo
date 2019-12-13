"""Check defaults.
"""
from __future__ import absolute_import

import unittest
import os

import sourceinfo.fileinfo


#
#######################
#
class CallUnits(unittest.TestCase):

    def testcase002(self):
        import sys
        _s=sys.path[:]
        sys.path.insert(0,os.path.abspath(os.path.dirname(__file__)+os.sep+'..'))
        import fileinfo_check_usecases #@UnresolvedImport
        
        fpn = os.path.abspath(os.path.normpath(os.path.dirname(__file__)))
        fx = fileinfo_check_usecases.check_callback(sourceinfo.fileinfo.getcaller_pathname,2)

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)

        assert os.path.normpath(fx) == fpn

    def testcase003(self):
        import sys
        _s=sys.path[:]
        sys.path.insert(0,os.path.abspath(os.path.dirname(__file__)+os.sep+'..'))
        import fileinfo_check_usecases #@UnresolvedImport
        
        fx = fileinfo_check_usecases.check_callback(sourceinfo.fileinfo.getcaller_pathname,3)

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)

        assert os.path.basename(fx) == 'unittest'



if __name__ == '__main__':
    unittest.main()
