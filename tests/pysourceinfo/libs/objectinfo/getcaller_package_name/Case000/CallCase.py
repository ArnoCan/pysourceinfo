"""Check defaults.
"""
from __future__ import absolute_import

import unittest
import os

from sourceinfo.objectinfo import getcaller_package_name
import sourceinfo.objectinfo

#
#######################
#


class CallUnits(unittest.TestCase):
    def testcase000(self):
        import sys
        _s = sys.path[:]
        sys.path.insert(0, os.path.dirname(__file__) +
                        os.sep + '..' + os.sep + '..')
        import objectinfo_check_tests  # @UnresolvedImport

        fpn = sourceinfo.__name__
        fx = objectinfo_check_tests.check_callback(getcaller_package_name, 0)

        [sys.path.pop() for x in range(len(sys.path))]  # @UnusedVariable
        sys.path.extend(_s)

        assert fx == fpn

    def testcase001(self):
        import sys
        _s = sys.path[:]
        sys.path.insert(0, os.path.dirname(__file__) +
                        os.sep + '..' + os.sep + '..')
        import objectinfo_check_tests  # @UnresolvedImport

        fx0 = objectinfo_check_tests.__name__
        fx1 = "tests"

        fx = objectinfo_check_tests.check_callback(getcaller_package_name, 1)

        [sys.path.pop() for x in range(len(sys.path))]  # @UnusedVariable
        sys.path.extend(_s)

        # due to PyUnit path resolution dependent on curdir
        assert fx == fx0 or fx == fx1

    def testcase002(self):
        import sys
        _s = sys.path[:]
        sys.path.insert(0, os.path.dirname(__file__) +
                        os.sep + '..' + os.sep + '..')
        import objectinfo_check_tests  # @UnresolvedImport

        fx0 = 'lib'
        fx1 = 'tests'
        fx = objectinfo_check_tests.check_callback(getcaller_package_name, 2)

        [sys.path.pop() for x in range(len(sys.path))]  # @UnusedVariable
        sys.path.extend(_s)

        assert fx == fx0 or fx == fx1

    def testcase003(self):
        import sys
        _s = sys.path[:]
        sys.path.insert(0, os.path.dirname(__file__) +
                        os.sep + '..' + os.sep + '..')
        import objectinfo_check_tests  # @UnresolvedImport

        fx = objectinfo_check_tests.check_callback(getcaller_package_name, 3)

        [sys.path.pop() for x in range(len(sys.path))]  # @UnusedVariable
        sys.path.extend(_s)

        assert fx == "unittest"


if __name__ == '__main__':
    unittest.main()
