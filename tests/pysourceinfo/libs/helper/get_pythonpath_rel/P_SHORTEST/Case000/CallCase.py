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

    def testcase020(self):
        sys.path.insert(0,  os.path.abspath(os.path.normpath(os.path.dirname(__file__) + '/a')))
        sys.path.insert(0,  os.path.abspath(os.path.normpath(os.path.dirname(__file__) + '/a/x0')))
        sys.path.insert(0,  os.path.abspath(os.path.normpath(os.path.dirname(__file__) + '/a/a2/x1')))

        resx = 'fileA.py'
        res = getpythonpath_rel('fileA.py', presolve=P_SHORTEST)
        self.assertEqual(res, resx)

    def testcase030(self):
        sys.path.insert(0,  os.path.abspath(os.path.normpath(os.path.dirname(__file__) + '/a')))
        sys.path.insert(0,  os.path.abspath(os.path.normpath(os.path.dirname(__file__) + '/a/x0')))
        sys.path.insert(0,  os.path.abspath(os.path.normpath(os.path.dirname(__file__) + '/a/a2/x1')))

        resx = 'x0/fileA.py'
        res = getpythonpath_rel('x0/fileA.py', presolve=P_SHORTEST)
        self.assertEqual(res, resx)

    def testcase040(self):
        sys.path.insert(0,  os.path.abspath(os.path.normpath(os.path.dirname(__file__) + '/a')))
        sys.path.insert(0,  os.path.abspath(os.path.normpath(os.path.dirname(__file__) + '/a/x0')))
        sys.path.insert(0,  os.path.abspath(os.path.normpath(os.path.dirname(__file__) + '/a/a2/x1')))

        resx = 'a2/x1/fileA.py'
        res = getpythonpath_rel('a2/x1/fileA.py', presolve=P_SHORTEST)
        self.assertEqual(res, resx)

    def testcase050(self):
        sys.path.insert(0,  os.path.abspath(os.path.normpath(os.path.dirname(__file__) + '/a')))
        sys.path.insert(0,  os.path.abspath(os.path.normpath(os.path.dirname(__file__) + '/a/x0')))
        sys.path.insert(0,  os.path.abspath(os.path.normpath(os.path.dirname(__file__) + '/a/a2/x1')))

        resx = 'fileA.py'
        res = getpythonpath_rel(
            os.path.abspath(os.path.normpath(os.path.dirname(__file__) + '/a/a2/x1/fileA.py')),
            presolve=P_SHORTEST
            )
        self.assertEqual(res, resx)


if __name__ == '__main__':
    unittest.main()
