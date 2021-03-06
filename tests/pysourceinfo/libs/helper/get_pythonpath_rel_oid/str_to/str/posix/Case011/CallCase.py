from __future__ import absolute_import

import sys
import os
import ntpath

import unittest

import sourceinfo
import sourceinfo.helper

import testdata.pysourceinfo


class CallUnits(unittest.TestCase):

    def setUp(self):
        sys.path.insert(
            0, 
            os.path.abspath(os.path.normpath(testdata.pysourceinfo.mypathname))
            )
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)
        sys.path.pop(0)

    def testcase000(self):
        _in = 'a/b/c'
        resx = 'a.b.c'

        res = sourceinfo.helper.getpythonpath_rel_oid(
            _in, 
            restype=sourceinfo.OID_STR,
#             sep='/',
#             normpath=os.path.normpath,
            )
        self.assertEqual(res, resx)


if __name__ == '__main__':
    unittest.main()
