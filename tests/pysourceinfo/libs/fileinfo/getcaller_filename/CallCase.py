"""Check defaults.
"""
from __future__ import absolute_import

import unittest
import os

import sourceinfo.fileinfo


#
#######################
#
class CallUnits(unittest.TestCase):
    def testcase000(self):
        import sys
        sys.path.insert(0, os.path.dirname(__file__) + os.sep + '..')
        import fileinfo_check_tests  # @UnresolvedImport

        fx = fileinfo_check_tests.check_callback(
            sourceinfo.fileinfo.getcaller_filename, 0)

        sys.path.pop(0)

        assert fx == 'fileinfo.py'

    def testcase001(self):
        import sys
        sys.path.insert(0, os.path.dirname(__file__) + os.sep + '..')
        import fileinfo_check_tests  # @UnresolvedImport

        fx = fileinfo_check_tests.check_callback(
            sourceinfo.fileinfo.getcaller_filename, 1)

        sys.path.pop(0)

        assert fx == 'fileinfo.py'

    def testcase002(self):
        import sys
        sys.path.insert(0, os.path.dirname(__file__) + os.sep + '..')
        import fileinfo_check_tests  # @UnresolvedImport

        fx = fileinfo_check_tests.check_callback(
            sourceinfo.fileinfo.getcaller_filename, 2)

        sys.path.pop(0)

        assert fx == 'fileinfo_check_tests.py'

    def testcase003(self):
        import sys
        sys.path.insert(0, os.path.dirname(__file__) + os.sep + '..')
        import fileinfo_check_tests  # @UnresolvedImport

        fx = fileinfo_check_tests.check_callback(
            sourceinfo.fileinfo.getcaller_filename, 3)

        sys.path.pop(0)

        assert fx == 'CallCase.py'


if __name__ == '__main__':
    unittest.main()
