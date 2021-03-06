"""Check defaults.
"""
from __future__ import absolute_import

import unittest
import os
import sys

version = '{0}.{1}'.format(*sys.version_info[:2])

import sourceinfo.fileinfo
import sourceinfo.objectinfo


#
#######################
#
class CallUnits(unittest.TestCase):
    def testcase000(self):
        import sys
        _s = sys.path[:]
        sys.path.insert(0, os.path.dirname(__file__))
        import check_linenumber_5  # @UnresolvedImport

        fx = check_linenumber_5.check_callback(
            sourceinfo.fileinfo.getcaller_linenumber, 1)

        sys.path.pop(0)
        assert sys.path == _s

        assert fx == 5


if __name__ == '__main__':
    unittest.main()
