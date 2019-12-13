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
        _s = sys.path[:]
        sys.path.insert(0, os.path.dirname(__file__))
        import check_linenumber_5  # @UnresolvedImport

        fx = check_linenumber_5.check_callback(
            sourceinfo.fileinfo.getcaller_linenumber, 1)

        sys.path.pop(0)
        assert sys.path == _s

        self.assertEqual(fx, 5)


if __name__ == '__main__':
    unittest.main()
