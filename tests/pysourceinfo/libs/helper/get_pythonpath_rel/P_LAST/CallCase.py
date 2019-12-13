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

    def testcase010(self):
        sys.path.append(
            os.path.abspath(os.path.normpath(os.path.dirname(__file__) + os.sep + '..'))
            )

        resx = 'P_LAST/CallCase.py'
        res = getpythonpath_rel('P_LAST/CallCase.py', presolve=P_LAST)
        self.assertEqual(res, resx)


if __name__ == '__main__':
    unittest.main()
