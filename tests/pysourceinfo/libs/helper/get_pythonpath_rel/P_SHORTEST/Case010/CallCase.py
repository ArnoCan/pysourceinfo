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

    def testcase060(self):
        sys.path.insert(0,  os.path.abspath(os.path.normpath(os.path.dirname(__file__))))

        resx = 'a/a2/x1/fileA.py'
        res = getpythonpath_rel(
            os.path.abspath(os.path.normpath(os.path.dirname(__file__) + '/a/a2/x1/fileA.py')),
            presolve=P_SHORTEST
            )
        self.assertEqual(res, resx)

    def testcase070(self):
        sys.path.insert(0,  os.path.abspath(os.path.normpath(os.path.dirname(__file__))))

        resx = 'a/x0/fileA.py'
        res = getpythonpath_rel(
            os.path.abspath(os.path.normpath(os.path.dirname(__file__) + '/a/x0/fileA.py')),
            presolve=P_SHORTEST
            )
        self.assertEqual(res, resx)


if __name__ == '__main__':
    unittest.main()
