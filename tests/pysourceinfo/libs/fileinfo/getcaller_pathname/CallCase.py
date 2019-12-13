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
        _s = sys.path[:]
        sys.path.insert(0, os.path.dirname(__file__) + os.sep + '..')
        import fileinfo_check_tests  # @UnresolvedImport

        fpn = sourceinfo.fileinfo.getmodule_pathname(sourceinfo.fileinfo)
        fpn = os.path.abspath(fpn)
        fx = fileinfo_check_tests.check_callback(
            sourceinfo.fileinfo.getcaller_pathname, 0)
        assert os.path.normpath(fx) == fpn

        [sys.path.pop() for x in range(len(sys.path))]  # @UnusedVariable
        sys.path.extend(_s)

    def testcase001(self):
        import sys
        _s = sys.path[:]
        sys.path.insert(0, os.path.dirname(__file__) + os.sep + '..')
        import fileinfo_check_tests  # @UnresolvedImport

        fx0 = sourceinfo.fileinfo.getmodule_pathname(fileinfo_check_tests)
        fx1 = sourceinfo.fileinfo.getmodule_pathname(sourceinfo)

        fx0 = os.path.abspath(fx0)
        fx1 = os.path.abspath(fx1)

        fx = fileinfo_check_tests.check_callback(
            sourceinfo.fileinfo.getcaller_pathname, 1)
        fx = os.path.normpath(fx)

        #self.assertEqual(fx, fx0)

        assert fx == fx0 or fx == fx1

        [sys.path.pop() for x in range(len(sys.path))]  # @UnusedVariable
        sys.path.extend(_s)

    def testcase002(self):
        import sys
        _s = sys.path[:]
        sys.path.insert(0, os.path.dirname(__file__) + os.sep + '..')
        import fileinfo_check_tests  # @UnresolvedImport

        fpn = os.path.abspath(os.path.normpath(os.path.dirname(__file__)))

        fx = fileinfo_check_tests.check_callback(
            sourceinfo.fileinfo.getcaller_pathname, 2)
        fx = os.path.normpath(fx)
        assert fx == fpn

        [sys.path.pop() for x in range(len(sys.path))]  # @UnusedVariable
        sys.path.extend(_s)

    def testcase003(self):
        import sys
        _s = sys.path[:]
        sys.path.insert(0, os.path.dirname(__file__) + os.sep + '..')
        import fileinfo_check_tests  # @UnresolvedImport

        fx = fileinfo_check_tests.check_callback(
            sourceinfo.fileinfo.getcaller_pathname, 3)
        version = '{0}.{1}'.format(*sys.version_info[:2])
        if version == '2.6':  # pragma: no cover
            assert os.path.basename(fx) == 'python2.6'
        elif version == '2.7':  # pragma: no cover
            assert os.path.basename(fx) == 'unittest'
        elif version >= '3.3':  # pragma: no cover
            assert os.path.basename(fx) == 'unittest'
        else:
            assert False

        [sys.path.pop() for x in range(len(sys.path))]  # @UnusedVariable
        sys.path.extend(_s)


if __name__ == '__main__':
    unittest.main()
