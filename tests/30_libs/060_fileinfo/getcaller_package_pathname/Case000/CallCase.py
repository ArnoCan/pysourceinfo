"""Check defaults.
"""
from __future__ import absolute_import

import unittest
import os

import pysourceinfo.fileinfo
import testdata


#
#######################
#
class CallUnits(unittest.TestCase):
    def testcase000(self):
        import sys
        _s = sys.path[:]
        sys.path.insert(0, os.path.dirname(__file__) +
                        os.sep + '..' + os.sep + '..')
        import fileinfo_check_tests  # @UnresolvedImport

        fpn = os.path.abspath(os.path.normpath(
            os.path.dirname(pysourceinfo.__file__) + "/.."))
        fx = fileinfo_check_tests.check_callback(
            pysourceinfo.fileinfo.getcaller_package_pathname, 0)
        fx = os.path.normpath(fx)
        self.assertEqual(fx, fpn)

        sys.path.pop(0)
        self.assertEqual(sys.path, _s)

    def testcase001(self):
        import sys
        _s = sys.path[:]

        fx00 = os.path.realpath(os.path.abspath(
            os.path.dirname(testdata.__file__) + os.sep + '..'))
        sys.path.insert(0, fx00)
        sys.path.insert(0, os.path.abspath(os.path.dirname(
            __file__) + os.sep + '..' + os.sep + '..'))

        import fileinfo_check_tests  # @UnresolvedImport
        fx = fileinfo_check_tests.check_callback(
            pysourceinfo.fileinfo.getcaller_package_pathname, 2)
        fx = os.path.realpath(os.path.normpath(fx))
        fxchk = fx[len(fx00):len(fx00 + os.path.sep + 'tests')]
        self.assertEqual(fxchk, os.path.sep + 'tests')

        sys.path.pop(0)
        sys.path.pop(0)
        self.assertEqual(sys.path, _s)

    def testcase002(self):
        import sys
        _s = sys.path[:]
        sys.path.insert(0, os.path.dirname(__file__) +
                        os.sep + '..' + os.sep + '..')
        import fileinfo_check_tests  # @UnresolvedImport

        fx3 = os.path.dirname(__file__) + os.sep + '..' + os.sep + '..'
        fx = fileinfo_check_tests.check_callback(
            pysourceinfo.fileinfo.getcaller_package_pathname, 2)
        fx = os.path.normpath(fx)

        fx3 = os.path.abspath(fx3)
        fx = os.path.abspath(fx)
        fx3 = os.path.normpath(os.path.normpath(fx3))
        fx = os.path.normpath(os.path.normpath(fx))

        assert fx == fx3

        sys.path.pop(0)
        self.assertEqual(sys.path, _s)

    def testcase003(self):
        import sys
        _s = sys.path[:]
        sys.path.insert(0, os.path.dirname(__file__) +
                        os.sep + '..' + os.sep + '..')
        import fileinfo_check_tests  # @UnresolvedImport

        fx = fileinfo_check_tests.check_callback(
            pysourceinfo.fileinfo.getcaller_package_pathname, 3)

        fp = os.path.normpath(os.path.dirname(unittest.__file__) + "/..")

        assert fx == fp

        sys.path.pop(0)
        assert sys.path == _s


if __name__ == '__main__':
    unittest.main()
