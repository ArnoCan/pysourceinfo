from __future__ import absolute_import

import unittest
import os
import sys

from sourceinfo import P_SHORTEST
from sourceinfo.helper import getpythonpath


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
        
        sys.path.insert(0,  os.path.abspath(os.path.normpath(os.path.dirname(__file__) + '/a')))
        sys.path.insert(0,  os.path.abspath(os.path.normpath(os.path.dirname(__file__) + '/a/x0')))
        sys.path.insert(0,  os.path.abspath(os.path.normpath(os.path.dirname(__file__) + '/a/a2/x1')))

        resx = os.path.abspath(os.path.normpath(os.path.dirname(__file__) + '/a'))
        res = getpythonpath('fileA.py', presolve=P_SHORTEST)
        self.assertEqual(res, resx)


if __name__ == '__main__':
    unittest.main()
