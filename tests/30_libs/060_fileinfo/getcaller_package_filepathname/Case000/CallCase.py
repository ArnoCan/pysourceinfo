"""Check defaults.
"""
from __future__ import absolute_import

import unittest
import os

import pysourceinfo.fileinfo


#
#######################
#
class CallUnits(unittest.TestCase):
    def testcase000(self):
        import sys
        _s = sys.path[:]
        _sx = repr(sys.path)
        sys.path.insert(0, os.path.dirname(__file__) +
                        os.sep + '..' + os.sep + '..')
        import fileinfo_check_tests  # @UnresolvedImport  # pylint: disable-msg=F0401

        fpn = pysourceinfo.fileinfo.getmodule_filepathname(
            fileinfo_check_tests)
        fx = fileinfo_check_tests.check_callback(
            pysourceinfo.fileinfo.getcaller_package_filepathname, 1)

        assert os.path.normpath(fx) == fpn
        assert _sx != repr(sys.path)
        sys.path.pop(0)
        assert _sx == repr(sys.path)


if __name__ == '__main__':
    unittest.main()
