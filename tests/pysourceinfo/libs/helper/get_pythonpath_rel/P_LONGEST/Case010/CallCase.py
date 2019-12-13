from __future__ import absolute_import

import unittest
import os
import sys

import sourceinfo  # @UnusedImport
from sourceinfo import P_LONGEST
from sourceinfo.helper import getpythonpath_rel


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
        sys.path.insert(0,  os.path.abspath(os.path.normpath(os.path.dirname(__file__) + '/a')))
        sys.path.insert(0,  os.path.abspath(os.path.normpath(os.path.dirname(__file__) + '/a/a2')))
        sys.path.insert(0,  os.path.abspath(os.path.normpath(os.path.dirname(__file__) + '/a/a2/a3')))

        resx = 'a2/x0/fileA.py'
        res = getpythonpath_rel(
            os.path.abspath(os.path.normpath(os.path.dirname(__file__) + '/a/a2/x0/fileA.py')),
            sys.path[:3],
            presolve=P_LONGEST
            )
        self.assertEqual(res, resx)

    def testcase070(self):
        sys.path.insert(0,  os.path.abspath(os.path.normpath(os.path.dirname(__file__))))
        sys.path.insert(0,  os.path.abspath(os.path.normpath(os.path.dirname(__file__) + '/a')))

        resx = 'a/x0/fileA.py'
        res = getpythonpath_rel(
            os.path.abspath(os.path.normpath(os.path.dirname(__file__) + '/a/x0/fileA.py')),
            sys.path[:2],
            presolve=P_LONGEST
            )
        self.assertEqual(res, resx)

    def testcase080(self):
        sys.path.insert(0,  os.path.abspath(os.path.normpath(os.path.dirname(__file__))))
        sys.path.insert(0,  os.path.abspath(os.path.normpath(os.path.dirname(__file__) + '/a')))
        sys.path.insert(0,  os.path.abspath(os.path.normpath(os.path.dirname(sourceinfo.__file__) + '/..' )))
        resx = 'tests/pysourceinfo/libs/helper/get_pythonpath_rel/P_LONGEST/Case010/a/x0/fileA.py'
        res = getpythonpath_rel(
            os.path.abspath(os.path.normpath(os.path.dirname(__file__) + '/a/x0/fileA.py')),
            sys.path[:3],
            presolve=P_LONGEST
            )
        self.assertEqual(res, resx)


if __name__ == '__main__':
    unittest.main()
