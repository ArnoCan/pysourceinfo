from __future__ import absolute_import

import unittest
import os

import pysourceinfo.fileinfo
import pysourceinfo.objectinfo


#
#######################
#
class CallUnits(unittest.TestCase):
    def testcase000(self):
        import sys
        _s = sys.path[:]
        sys.path.insert(0, os.path.dirname(__file__) + os.sep + '..')
        import fileinfo_check_tests  # @UnresolvedImport

        fpn = pysourceinfo.fileinfo.getmodule_filepathname(
            pysourceinfo.objectinfo)
        fm = fileinfo_check_tests.check_callback(
            pysourceinfo.objectinfo.getcaller_module, 0)
        fx = pysourceinfo.fileinfo.getmodule_filepathname(fm)

        assert os.path.normpath(fx) == fpn

        [sys.path.pop() for x in range(len(sys.path))]  # @UnusedVariable
        sys.path.extend(_s)

    def testcase001(self):
        import sys
        _s = sys.path[:]
        sys.path.insert(0, os.path.dirname(__file__) + os.sep + '..')
        import fileinfo_check_tests  # @UnresolvedImport

        fpn = pysourceinfo.fileinfo.getmodule_filepathname(
            fileinfo_check_tests)
        fm = fileinfo_check_tests.check_callback(
            pysourceinfo.objectinfo.getcaller_module, 1)
        fx = pysourceinfo.fileinfo.getmodule_filepathname(fm)

        assert os.path.normpath(fx) == fpn

        [sys.path.pop() for x in range(len(sys.path))]  # @UnusedVariable
        sys.path.extend(_s)

    def testcase002(self):
        import sys
        _s = sys.path[:]
        sys.path.insert(0, os.path.dirname(__file__) + os.sep + '..')
        import fileinfo_check_tests  # @UnresolvedImport

        fpn = os.path.abspath(os.path.normpath(__file__))
        if fpn[-4:-1] == '.py':
            fpn = fpn[:-1]
        fm = fileinfo_check_tests.check_callback(
            pysourceinfo.objectinfo.getcaller_module, 2)
        fx = pysourceinfo.fileinfo.getmodule_filepathname(fm)

        assert os.path.normpath(fx) == fpn

        [sys.path.pop() for x in range(len(sys.path))]  # @UnusedVariable
        sys.path.extend(_s)

    def testcase003(self):
        import sys
        _s = sys.path[:]
        sys.path.insert(0, os.path.dirname(__file__) + os.sep + '..')
        import fileinfo_check_tests  # @UnresolvedImport

        fm = fileinfo_check_tests.check_callback(
            pysourceinfo.objectinfo.getcaller_module, 3)
        fx = pysourceinfo.fileinfo.getmodule_filepathname(fm)
        fx = os.path.basename(fx)

        version = '{0}.{1}'.format(*sys.version_info[:2])
        assert os.path.basename(fx) == 'case.py'

        [sys.path.pop() for x in range(len(sys.path))]  # @UnusedVariable
        sys.path.extend(_s)


if __name__ == '__main__':
    unittest.main()
