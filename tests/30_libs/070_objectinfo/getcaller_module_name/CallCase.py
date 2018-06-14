"""Check defaults.
"""
from __future__ import absolute_import

import unittest
import os

import pysourceinfo.objectinfo


#
#######################
#
class CallUnits(unittest.TestCase):
    def testcase000(self):
        import sys
        _s = sys.path[:]
        sys.path.insert(0, os.path.dirname(__file__) + os.sep + '..')
        import objectinfo_check_tests  # @UnresolvedImport

        import inspect
        _is = inspect.getsourcefile(objectinfo_check_tests)

        fx = objectinfo_check_tests.check_callback(
            pysourceinfo.objectinfo.getcaller_module_name, 0)

        [sys.path.pop() for x in range(len(sys.path))]  # @UnusedVariable
        sys.path.extend(_s)

        assert fx == 'pysourceinfo.objectinfo'

    def testcase001(self):
        import sys
        _s = sys.path[:]
        sys.path.insert(0, os.path.dirname(__file__) + os.sep + '..')
        import objectinfo_check_tests  # @UnresolvedImport

        fx = objectinfo_check_tests.check_callback(
            pysourceinfo.objectinfo.getcaller_module_name, 1)
        fx0 = "objectinfo_check_tests"
        fx1 = "tests.30_libs.070_objectinfo.objectinfo_check_tests"

        # due to PyUnit path resolution dependent on curdir

        [sys.path.pop() for x in range(len(sys.path))]  # @UnusedVariable
        sys.path.extend(_s)

        assert fx == fx0 or fx == fx1

    def testcase002(self):
        import sys
        _s = sys.path[:]
        sys.path.insert(0, os.path.dirname(__file__) + os.sep + '..')
        import objectinfo_check_tests  # @UnresolvedImport

        fx0 = 'tests.30_libs.070_objectinfo.getcaller_module_name.CallCase'
        fx1 = '30_libs.070_objectinfo.getcaller_module_name.CallCase'
        fx = objectinfo_check_tests.check_callback(
            pysourceinfo.objectinfo.getcaller_module_name, 2)

        [sys.path.pop() for x in range(len(sys.path))]  # @UnusedVariable
        sys.path.extend(_s)

        assert fx == fx0 or fx == fx1

    def testcase003(self):
        import sys
        _s = sys.path[:]
        sys.path.insert(0, os.path.dirname(__file__) + os.sep + '..')
        import objectinfo_check_tests  # @UnresolvedImport

        fx = objectinfo_check_tests.check_callback(
            pysourceinfo.objectinfo.getcaller_module_name, 3)

        [sys.path.pop() for x in range(len(sys.path))]  # @UnusedVariable
        sys.path.extend(_s)

        version = '{0}.{1}'.format(*sys.version_info[:2])
        if version == '2.6':  # pragma: no cover
            assert os.path.basename(fx) == 'unittest'
        elif version == '2.7':  # pragma: no cover
            assert fx == 'unittest.case'
        elif version >= '3.3':  # pragma: no cover
            assert fx == 'unittest.case'
        else:
            assert False

    def testcase004(self):
        import sys
        _s = sys.path[:]
        sys.path.insert(0, os.path.dirname(__file__) + os.sep + '..')
        import objectinfo_check_tests  # @UnresolvedImport

        fx = objectinfo_check_tests.check_callback(
            pysourceinfo.objectinfo.getcaller_module_name, 4)

        [sys.path.pop() for x in range(len(sys.path))]  # @UnusedVariable
        sys.path.extend(_s)

        version = '{0}.{1}'.format(*sys.version_info[:2])
        if version == '2.6':  # pragma: no cover
            assert os.path.basename(fx) == 'unittest'
        elif version == '2.7':  # pragma: no cover
            assert fx == 'unittest.case'
        elif version >= '3.3':  # pragma: no cover
            assert fx == 'unittest.case'
        else:
            assert False


if __name__ == '__main__':
    unittest.main()
