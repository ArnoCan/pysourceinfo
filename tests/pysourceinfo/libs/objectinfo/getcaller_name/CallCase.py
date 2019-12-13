"""Check defaults.
"""
from __future__ import absolute_import

import unittest
import os

from sourceinfo.objectinfo import getcaller_name

#
#######################
#


class CallUnits(unittest.TestCase):
    def testcase000(self):
        import sys
        _s = sys.path[:]
        sys.path.insert(0, os.path.dirname(__file__) + os.sep + '..')
        import objectinfo_check_tests  # @UnresolvedImport

        fx = objectinfo_check_tests.check_callback(getcaller_name, 0)

        [sys.path.pop() for x in range(len(sys.path))]  # @UnusedVariable
        sys.path.extend(_s)

        assert fx == 'getcaller_name'

    def testcase001(self):
        import sys
        _s = sys.path[:]
        sys.path.insert(0, os.path.dirname(__file__) + os.sep + '..')
        import objectinfo_check_tests  # @UnresolvedImport

        fx = objectinfo_check_tests.check_callback(getcaller_name, 1)

        [sys.path.pop() for x in range(len(sys.path))]  # @UnusedVariable
        sys.path.extend(_s)

        assert fx == 'check_callback'

    def testcase002(self):
        import sys
        _s = sys.path[:]
        sys.path.insert(0, os.path.dirname(__file__) + os.sep + '..')
        import objectinfo_check_tests  # @UnresolvedImport

        fx = objectinfo_check_tests.check_callback(getcaller_name, 2)

        [sys.path.pop() for x in range(len(sys.path))]  # @UnusedVariable
        sys.path.extend(_s)

        assert fx == 'testcase002'

    def testcase003(self):
        import sys
        _s = sys.path[:]
        sys.path.insert(0, os.path.dirname(__file__) + os.sep + '..')
        import objectinfo_check_tests  # @UnresolvedImport

        fx = objectinfo_check_tests.check_callback(getcaller_name, 3)

        [sys.path.pop() for x in range(len(sys.path))]  # @UnusedVariable
        sys.path.extend(_s)

        assert fx == 'run'


if __name__ == '__main__':
    unittest.main()
