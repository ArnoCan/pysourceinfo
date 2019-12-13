"""Check defaults.
"""
from __future__ import absolute_import

import unittest
import os
import sys

import sourceinfo.fileinfo


#
#######################
#
class CallUnits(unittest.TestCase):
    def testcase000(self):
        import testdata.pysourceinfo
        sys.path.insert(0, os.path.normpath(testdata.pysourceinfo.mypath))
        fpn = sourceinfo.fileinfo.getcaller_pathname_rel()

        res = os.path.normpath(fpn)
        resx = os.path.normpath('tests/pysourceinfo/libs/fileinfo/getcaller_pathname_rel')
        
        self.assertEqual(res, resx)


if __name__ == '__main__':
    unittest.main()
