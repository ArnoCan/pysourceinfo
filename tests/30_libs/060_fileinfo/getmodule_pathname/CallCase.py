"""Check defaults.
"""
from __future__ import absolute_import

import unittest
import os

import pysourceinfo.fileinfo
from testdata import mypath

#
#######################
#


class CallUnits(unittest.TestCase):
    def testcase000(self):
        import sys
        _s = sys.path[:]
        sys.path.insert(0, os.path.dirname(__file__) + os.sep + '..')
        import fileinfo_check_tests  # @UnresolvedImport

        fpn = pysourceinfo.fileinfo.getmodule_pathname(pysourceinfo.fileinfo)

        fm = fileinfo_check_tests.check_callback(
            pysourceinfo.objectinfo.getcaller_module, 0)
        fx = pysourceinfo.fileinfo.getmodule_pathname(fm)

        assert os.path.normpath(fx) == fpn

        [sys.path.pop() for x in range(len(sys.path))]  # @UnusedVariable
        sys.path.extend(_s)

    def testcase001(self):
        import sys
        _s = sys.path[:]
        sys.path.insert(0, os.path.dirname(__file__) + os.sep + '..')
        import fileinfo_check_tests  # @UnresolvedImport

        fpn = pysourceinfo.fileinfo.getmodule_pathname(fileinfo_check_tests)

        fm = fileinfo_check_tests.check_callback(
            pysourceinfo.objectinfo.getcaller_module, 1)
        fx = pysourceinfo.fileinfo.getmodule_pathname(fm)

        assert os.path.normpath(fx) == fpn

        [sys.path.pop() for x in range(len(sys.path))]  # @UnusedVariable
        sys.path.extend(_s)

    def testcase002(self):
        import sys
        _s = sys.path[:]
        import fileinfo_check_tests  # @UnresolvedImport

        fm = fileinfo_check_tests.check_callback(
            pysourceinfo.objectinfo.getcaller_module, 2)
        fx = pysourceinfo.fileinfo.getmodule_pathname(fm)

        fm = os.path.dirname(os.path.normpath(fm.__file__))
        fx = os.path.normpath(fx)
        assert fx == fm

        [sys.path.pop() for x in range(len(sys.path))]  # @UnusedVariable
        sys.path.extend(_s)

    def testcase003(self):
        import sys
        _s = sys.path[:]
        sys.path.insert(0, os.path.dirname(__file__) + os.sep + '..')
        import fileinfo_check_tests  # @UnresolvedImport

        fm = fileinfo_check_tests.check_callback(
            pysourceinfo.objectinfo.getcaller_module, 3)
        fx = pysourceinfo.fileinfo.getmodule_pathname(fm)
        fx = os.path.basename(fx)

        version = '{0}.{1}'.format(*sys.version_info[:2])
        if version == '2.6':  # pragma: no cover
            assert os.path.basename(fx) == 'python2.6'
        elif version == '2.7':  # pragma: no cover
            assert os.path.basename(fx) == 'unittest'
        elif version >= '3.3':  # pragma: no cover
            if fx.endswith('__init__.py'):
                assert os.path.basename(os.path.dirname(fx)) == "unittest"
            else:
                assert os.path.basename(fx) == "unittest"
        else:
            assert False

        [sys.path.pop() for x in range(len(sys.path))]  # @UnusedVariable
        sys.path.extend(_s)


if __name__ == '__main__':
    unittest.main()
