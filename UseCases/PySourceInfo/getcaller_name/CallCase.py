"""Check defaults.
"""
from __future__ import absolute_import

import unittest
import os

from pysourceinfo.objectinfo import getcaller_name

#
#######################
#
class CallUnits(unittest.TestCase):

    def testcase002(self):
        import sys
        _s=sys.path[:]
        sys.path.insert(0,os.path.abspath(os.path.dirname(__file__)+os.sep+'..'))
        import PySourceInfo_check #@UnresolvedImport
        
        fx = PySourceInfo_check.check_callback(getcaller_name,2)

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)

        assert fx == 'testcase002'

if __name__ == '__main__':
    unittest.main()
