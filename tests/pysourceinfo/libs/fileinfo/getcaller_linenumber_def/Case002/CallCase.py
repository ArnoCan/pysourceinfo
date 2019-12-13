"""Check defaults.
"""
from __future__ import absolute_import

import unittest
import os
import sys

version = '{0}.{1}'.format(*sys.version_info[:2])

import sourceinfo.fileinfo


#
#######################
#
class CallUnits(unittest.TestCase):
    def testcase000(self):
        _s = sys.path[:]
        sys.path.insert(0, os.path.dirname(__file__))
        import check_linenumber_10_10  # @UnresolvedImport

        fx = check_linenumber_10_10.check_callback(
            sourceinfo.fileinfo.getcaller_linenumber_def, 1)

        sys.path.pop(0)
        assert sys.path == _s

        self.assertEqual(fx, 10)


if __name__ == '__main__':
    unittest.main()
