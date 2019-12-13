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
        
        fx = fileinfo_check_usecases.check_callback(sourceinfo.fileinfo.getcaller_linenumber,2)

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)

        assert fx == 22

if __name__ == '__main__':
    unittest.main()
