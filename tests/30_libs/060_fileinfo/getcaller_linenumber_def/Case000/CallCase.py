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
        _s = sys.path[:]
        sys.path.insert(0, os.path.dirname(__file__) +
                        os.sep + '..' + os.sep + '..')
        import fileinfo_check_tests  # @UnresolvedImport

        fx = fileinfo_check_tests.check_callback(
            pysourceinfo.fileinfo.getcaller_linenumber_def, 0)

        sys.path.pop(0)

        assert fx > 50 and fx < 200
        assert sys.path == _s

    def testcase001(self):
        _s = sys.path[:]
        sys.path.insert(0, os.path.dirname(__file__) +
                        os.sep + '..' + os.sep + '..')
        import fileinfo_check_tests  # @UnresolvedImport

        fx = fileinfo_check_tests.check_callback(
            pysourceinfo.fileinfo.getcaller_linenumber_def, 1)

        sys.path.pop(0)

        self.assertEqual(fx, 4)
        assert sys.path == _s

    def testcase002(self):
        _s = sys.path[:]
        sys.path.insert(0, os.path.dirname(__file__) +
                        os.sep + '..' + os.sep + '..')
        import fileinfo_check_tests  # @UnresolvedImport

        fx = fileinfo_check_tests.check_callback(
            pysourceinfo.fileinfo.getcaller_linenumber_def, 2)

        sys.path.pop(0)

        self.assertEqual(fx, 47)
        assert sys.path == _s

    def testcase003(self):
        _s = sys.path[:]
        sys.path.insert(0, os.path.dirname(__file__) +
                        os.sep + '..' + os.sep + '..')
        import fileinfo_check_tests  # @UnresolvedImport

        global version
        if version >= '3.3':  # pragma: no cover
            fxn = fileinfo_check_tests.check_callback(
                pysourceinfo.objectinfo.getcaller_name, 4)
        else:
            fxn = fileinfo_check_tests.check_callback(
                pysourceinfo.objectinfo.getcaller_name, 3)
        fx = fileinfo_check_tests.check_callback(
            pysourceinfo.fileinfo.getcaller_linenumber_def, 3)

        sys.path.pop(0)
        assert sys.path == _s

        if version >= '3.3':  # pragma: no cover
            assert fxn == '__call__'
        else:
            assert fxn == 'run'

        version = '{0}.{1}'.format(*sys.version_info[:2])
        if version == '2.6':  # pragma: no cover
            # depends on platform, may require additional, anyhow keep it as a ref
            assert fx > 250 and fx < 300
        elif version == '2.7':  # pragma: no cover
            # depends on platform, may require additional, anyhow keep it as a ref
            assert fx > 200 and fx < 400
        elif version >= '3.3':  # pragma: no cover
            # depends on platform, may require additional, anyhow keep it as a ref
            assert fx > 400 and fx < 600
        else:
            assert False


if __name__ == '__main__':
    unittest.main()
