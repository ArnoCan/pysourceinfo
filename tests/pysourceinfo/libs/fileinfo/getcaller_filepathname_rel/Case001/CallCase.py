"""Check defaults.
"""
from __future__ import absolute_import

import unittest
import os
import sys
version = '{0}.{1}'.format(*sys.version_info[:2])

from pythonids.pythondist import PYDIST, PYE_DIST, PYE_JYTHON

import sourceinfo.fileinfo


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
        import fileinfo_check_tests  # @UnresolvedImport

        fpn = sourceinfo.fileinfo.getmodule_filepathname(
            sourceinfo.fileinfo)
        fx = fileinfo_check_tests.check_callback(
            sourceinfo.fileinfo.getcaller_filepathname, 0)
        assert os.path.normpath(fx) == fpn
        assert _sx != repr(sys.path)
        sys.path.pop(0)
        assert _sx == repr(sys.path)

        [sys.path.pop() for x in range(len(sys.path))]  # @UnusedVariable
        sys.path.extend(_s)

    def testcase001(self):
        import sys
        _s = sys.path[:]
        _sx = repr(sys.path)
        sys.path.insert(0, os.path.dirname(__file__) +
                        os.sep + '..' + os.sep + '..')
        import fileinfo_check_tests  # @UnresolvedImport

        fpn = sourceinfo.fileinfo.getmodule_filepathname(
            fileinfo_check_tests)
        fx = fileinfo_check_tests.check_callback(
            sourceinfo.fileinfo.getcaller_filepathname, 1)
        assert os.path.normpath(fx) == fpn
        assert _sx != repr(sys.path)
        sys.path.pop(0)
        assert _sx == repr(sys.path)

        [sys.path.pop() for x in range(len(sys.path))]  # @UnusedVariable
        sys.path.extend(_s)

    def testcase002(self):
        import sys
        _s = sys.path[:]
        _sx = repr(sys.path)
        sys.path.insert(0, os.path.dirname(__file__) +
                        os.sep + '..' + os.sep + '..')
        import fileinfo_check_tests  # @UnresolvedImport

        fpn = os.path.abspath(os.path.normpath(__file__))
        if PYDIST & PYE_DIST == PYE_JYTHON:
            if fpn.endswith('$py.class'):
                fpn = fpn[:-9] + '.py'
            if fpn.endswith('$py.clpy'):
                fpn = fpn[:-8] + '.py'
        else:
            if fpn[-4:-1] == '.py':
                fpn = fpn[:-1]

        fx = fileinfo_check_tests.check_callback(
            sourceinfo.fileinfo.getcaller_filepathname, 2)

        assert os.path.normpath(fx) == fpn
        assert _sx != repr(sys.path)
        sys.path.pop(0)
        assert _sx == repr(sys.path)

        [sys.path.pop() for x in range(len(sys.path))]  # @UnusedVariable
        sys.path.extend(_s)

    def testcase003(self):
        import sys
        _s = sys.path[:]
        _sx = repr(sys.path)
        sys.path.insert(0, os.path.dirname(__file__) +
                        os.sep + '..' + os.sep + '..')
        import fileinfo_check_tests  # @UnresolvedImport

        fx = fileinfo_check_tests.check_callback(
            sourceinfo.fileinfo.getcaller_filepathname, 3)
        assert os.path.basename(fx) == 'case.py'

        assert _sx != repr(sys.path)
        sys.path.pop(0)
        assert _sx == repr(sys.path)

        [sys.path.pop() for x in range(len(sys.path))]  # @UnusedVariable
        sys.path.extend(_s)


if __name__ == '__main__':
    unittest.main()
