"""Check defaults.
"""
from __future__ import absolute_import

import unittest
import os
import sys

import pysourceinfo.fileinfo


#
#######################
#
class CallUnits(unittest.TestCase):
    def testcase000(self):
        import testdata
        sys.path.insert(0, os.path.normpath(testdata.mypath))
        fpn = pysourceinfo.fileinfo.getcaller_pathname_rel()
        assert os.path.normpath(fpn) == os.path.normpath(
            'tests/30_libs/060_fileinfo/getcaller_pathname_rel')


if __name__ == '__main__':
    unittest.main()
