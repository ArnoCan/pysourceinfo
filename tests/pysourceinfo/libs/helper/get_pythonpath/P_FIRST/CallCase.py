from __future__ import absolute_import

import unittest
import os
import sys
import re

import sourceinfo.infolists
from sourceinfo import P_FIRST, P_LAST, P_SHORTEST, P_LONGEST
from sourceinfo.helper import getpythonpath, getpythonpath_rel


#
#######################
#
class CallUnits(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)
        sys.path.pop(0)

    def testcase000(self):
        mypath = os.path.abspath(os.path.normpath(os.path.dirname(__file__) + os.sep + '..')) 
        sys.path.insert(0, mypath)

        res = getpythonpath('P_FIRST/CallCase.py', presolve=P_FIRST)
        self.assertEqual(res, mypath)


if __name__ == '__main__':
    unittest.main()
