"""Check defaults.
"""
from __future__ import absolute_import

import unittest
import os
import sys

import pysourceinfo.fileinfo
import testdata


#
#######################
#
class CallUnits(unittest.TestCase):
    def testcase000(self):
        ppn = pysourceinfo.fileinfo.getcaller_package_pathname()
        sys.path.insert(0, testdata.mypath)
        fpn = pysourceinfo.fileinfo.getcaller_pathname_sub()
        p = ppn + os.path.sep + "tests" + os.path.sep + fpn
        f = os.path.dirname(os.path.abspath(__file__))
        self.assertEqual(p, f)


if __name__ == '__main__':
    unittest.main()
