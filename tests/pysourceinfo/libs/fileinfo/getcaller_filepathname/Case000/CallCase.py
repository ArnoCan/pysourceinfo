"""Check defaults.
"""
from __future__ import absolute_import

import unittest
import os

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
        if fpn and fpn[-3:] != '.py':
            fpn = fpn[:-3] + 'py'
        fx = fileinfo_check_tests.check_callback(
            sourceinfo.fileinfo.getcaller_filepathname, 0)
        if fx[-4:-1] == '.py':
            _c = fx[-1]
        else:
            _c = ''
        assert os.path.normpath(fx) == fpn + _c
        sys.path.pop(0)
        assert _sx == repr(sys.path)

    def testcase001(self):
        import sys
        _s = sys.path[:]
        _sx = repr(sys.path)
        sys.path.insert(0, os.path.dirname(__file__) +
                        os.sep + '..' + os.sep + '..')
        import fileinfo_check_tests  # @UnresolvedImport

        fpn = sourceinfo.fileinfo.getmodule_filepathname(
            fileinfo_check_tests)
        if fpn and fpn[-3:] != '.py':
            fpn = fpn[:-3] + 'py'

        fx = fileinfo_check_tests.check_callback(
            sourceinfo.fileinfo.getcaller_filepathname, 1)
        if fx[-4:-1] == '.py':
            _c = fx[-1]
        else:
            _c = ''
        assert os.path.normpath(fx) == fpn + _c
        assert _sx != repr(sys.path)
        sys.path.pop(0)
        assert _sx == repr(sys.path)

    def testcase002(self):
        import sys
        _s = sys.path[:]
        _sx = repr(sys.path)
        sys.path.insert(0, os.path.dirname(__file__) +
                        os.sep + '..' + os.sep + '..')
        import fileinfo_check_tests  # @UnresolvedImport

        fpn = os.path.abspath(os.path.normpath(__file__))
        if fpn and fpn[-3:] != '.py':
            fpn = fpn[:-3] + 'py'
        fx = fileinfo_check_tests.check_callback(
            sourceinfo.fileinfo.getcaller_filepathname, 2)
        
        if PYDIST & PYE_DIST == PYE_JYTHON:
            if fpn.endswith('$py.class'):
                fpn = fpn[:-9] + '.py'
            if fpn.endswith('$py.clpy'):
                fpn = fpn[:-8] + '.py'
        else:
            if fpn[-4:-1] == '.py':
                fpn = fpn[:-1]

        assert os.path.normpath(fx) == fpn
        assert _sx != repr(sys.path)
        sys.path.pop(0)
        assert _sx == repr(sys.path)

    def testcase003(self):
        import sys
        _s = sys.path[:]
        _sx = repr(sys.path)
        sys.path.insert(0, os.path.dirname(__file__) +
                        os.sep + '..' + os.sep + '..')
        import fileinfo_check_tests  # @UnresolvedImport

        fx = fileinfo_check_tests.check_callback(
            sourceinfo.fileinfo.getcaller_filepathname, 3)
        if fx[-4:-1] == '.py':
            _c = fx[-1]
        else:
            _c = ''
        version = '{0}.{1}'.format(*sys.version_info[:2])
        if version == '2.6':  # pragma: no cover
            assert os.path.basename(fx) == 'unittest.py' + _c
        elif version == '2.7':  # pragma: no cover
            assert os.path.basename(fx) == 'case.py' + _c
        elif version >= '3.3':  # pragma: no cover
            assert os.path.basename(fx) == 'case.py' + _c
        else:
            assert False

        assert _sx != repr(sys.path)
        sys.path.pop(0)
        assert _sx == repr(sys.path)


if __name__ == '__main__':
    unittest.main()
