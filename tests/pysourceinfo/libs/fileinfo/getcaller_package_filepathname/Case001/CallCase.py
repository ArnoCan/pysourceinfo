"""Check defaults.
"""
from __future__ import absolute_import
from __future__ import print_function

import unittest
import os

from pythonids.pythondist import PYDIST, PYE_DIST, PYE_JYTHON

import sourceinfo.fileinfo
import testdata.pysourceinfo


#
#######################
#
class CallUnits(unittest.TestCase):
    def testcase000(self):
        import sys
        _s = sys.path[:]
        
        sys.path.insert(
            0, 
            os.path.abspath(os.path.normpath(os.path.dirname(__file__) + os.sep + '..' + os.sep + '..'))
            )

        import fileinfo_check_tests  # @UnresolvedImport
        fpn = os.path.abspath(fileinfo_check_tests.__file__)

        if PYDIST & PYE_DIST == PYE_JYTHON:
            if fpn.endswith('$py.class'):
                fpn = fpn[:-9] + '.py'
        else:
            if fpn[-4:-1] == '.py':
                fpn = fpn[:-1]

        fx = fileinfo_check_tests.check_callback(
            sourceinfo.fileinfo.getcaller_package_filepathname, 1)
        fx = os.path.normpath(fx)

        sys.path.pop(0)
        self.assertEqual(sys.path, _s)
        self.assertEqual(fx, fpn)

    def testcase010(self):
        import sys
        _s = sys.path[:]

        fx00 = os.path.realpath(os.path.abspath(
            os.path.abspath(os.path.normpath(os.path.dirname(testdata.pysourceinfo.__file__) + os.sep + '..' + os.sep + '..')))
        )
        sys.path.insert(0, fx00)
        sys.path.insert(
            0,
            os.path.abspath(os.path.normpath(os.path.abspath(os.path.dirname(__file__) + os.sep + '..' + os.sep + '..')))
        )

        import fileinfo_check_tests  # @UnresolvedImport
        fx = fileinfo_check_tests.check_callback(
            sourceinfo.fileinfo.getcaller_package_filepathname, 2)
        fx = os.path.realpath(os.path.normpath(fx))
        fxchk = fx[len(fx00):len(fx00 + os.path.sep + 'tests')]
        self.assertEqual(fxchk, os.path.sep + 'tests')

        sys.path.pop(0)
        sys.path.pop(0)
        self.assertEqual(sys.path, _s)

    def testcase020(self):
        #
        # Depends on the call.
        #
        import sys
        _s = sys.path[:]
        sys.path.insert(
            0, 
            os.path.abspath(os.path.normpath(os.path.dirname(__file__) + os.sep + '..' + os.sep + '..'))
        )
        sys.path.insert(
            0,
            os.path.abspath(os.path.dirname(__file__))
        )

        import fileinfo_check_tests  # @UnresolvedImport

        fx4 = __file__
        fx = fileinfo_check_tests.check_callback(
            sourceinfo.fileinfo.getcaller_package_filepathname, 2)
        fx = os.path.normpath(fx)
        fx4 = os.path.abspath(fx4)
        fx = os.path.abspath(fx)
        fx4 = os.path.normpath(os.path.normpath(fx4))
        fx = os.path.normpath(os.path.normpath(fx))

        sys.path.pop(0)
        sys.path.pop(0)
        self.assertEqual(sys.path, _s)

        if PYDIST & PYE_DIST == PYE_JYTHON:
            if fx4.endswith('$py.class'):
                fx4 = fx4[:-9] + '.py'
        else:
            if fx4[-4:-1] == '.py':
                fx4 = fx4[:-1]

        assert fx == fx4  

    def testcase021(self):
        #
        # Depends on the call.
        #
        import sys
        _s = sys.path[:]
        sys.path.insert(
            0,
            os.path.abspath(os.path.normpath(os.path.dirname(__file__) +os.sep + '..' + os.sep + '..'))
        )
        sys.path.insert(
            0,
            os.path.abspath(os.path.normpath(os.path.dirname(__file__) + os.sep + '..'))
        )
        
        import fileinfo_check_tests  # @UnresolvedImport

        fx3 = os.path.dirname(__file__)
        fx = fileinfo_check_tests.check_callback(
            sourceinfo.fileinfo.getcaller_package_filepathname, 2)
        fx = os.path.normpath(fx)
        fx3 = os.path.abspath(fx3)
        fx = os.path.abspath(fx)
        fx3 = os.path.normpath(os.path.normpath(fx3))
        fx = os.path.normpath(os.path.normpath(fx))

        sys.path.pop(0)
        sys.path.pop(0)
        self.assertEqual(sys.path, _s)
        assert fx == fx3

    def testcase022(self):
        #
        # Depends on the call.
        #
        import sys
        _s = sys.path[:]
        sys.path.insert(
            0, 
            os.path.abspath(os.path.normpath(os.path.dirname(__file__) + os.sep + '..' + os.sep + '..'))
        )

        import fileinfo_check_tests  # @UnresolvedImport
        fx = fileinfo_check_tests.check_callback(
            sourceinfo.fileinfo.getcaller_package_filepathname, 2)
        fx = os.path.normpath(fx)
        fx = os.path.abspath(fx)
        fx = os.path.normpath(os.path.normpath(fx))

        fx2 = os.path.normpath(os.path.dirname(__file__) + os.sep + "..")

        fx2 = os.path.abspath(fx2)
        fx2 = os.path.normpath(os.path.normpath(fx2))
        
        sys.path.pop(0)
        self.assertEqual(sys.path, _s)
        self.assertEqual(fx, fx2)

    def testcase030(self):
        import sys
        _s = sys.path[:]
        sys.path.insert(
            0,
            os.path.abspath(os.path.normpath(os.path.dirname(__file__) + os.sep + '..' + os.sep + '..'))
        )

        import fileinfo_check_tests  # @UnresolvedImport
        fx = fileinfo_check_tests.check_callback(
            sourceinfo.fileinfo.getcaller_package_filepathname, 3)

        sys.path.pop(0)
        self.assertEqual(sys.path, _s)

        version = '{0}.{1}'.format(*sys.version_info[:2])
        if version == '2.6':  # pragma: no cover
            self.assertEqual(os.path.basename(fx), "unittest.py")
        elif version == '2.7':  # pragma: no cover
            assert os.path.basename(fx) == "unittest"
        elif version >= '3.3':  # pragma: no cover
            assert os.path.basename(fx) == "unittest"
        else:
            assert False


if __name__ == '__main__':
    unittest.main()
