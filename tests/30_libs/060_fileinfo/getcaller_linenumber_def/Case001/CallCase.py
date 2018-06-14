"""Check defaults.
"""
from __future__ import absolute_import

import unittest
import os
import sys

version = '{0}.{1}'.format(*sys.version_info[:2])

import pysourceinfo.fileinfo
import pysourceinfo.objectinfo


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
            pysourceinfo.fileinfo.getcaller_linenumber_def, 1)

        sys.path.pop(0)
        assert sys.path == _s

        assert fx == 4


if __name__ == '__main__':
    unittest.main()
