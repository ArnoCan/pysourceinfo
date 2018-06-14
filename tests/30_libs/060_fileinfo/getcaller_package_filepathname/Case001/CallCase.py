"""Check defaults.
"""
from __future__ import absolute_import
from __future__ import print_function

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

        fpn = os.path.abspath(fileinfo_check_tests.__file__)
        if fpn[-2] == 'y':
            fpn = fpn[:-1]  # this handles source files

        fx = fileinfo_check_tests.check_callback(
            pysourceinfo.fileinfo.getcaller_package_filepathname, 1)
        fx = os.path.normpath(fx)

        sys.path.pop(0)
        self.assertEqual(sys.path, _s)

        self.assertEqual(fx, fpn)

    def testcase010(self):
        import sys
        _s = sys.path[:]

        fx00 = os.path.realpath(os.path.abspath(
            os.path.dirname(testdata.__file__) + os.sep + '..'))
        sys.path.insert(0, fx00)
        sys.path.insert(0, os.path.abspath(os.path.dirname(
            __file__) + os.sep + '..' + os.sep + '..'))

        import fileinfo_check_tests  # @UnresolvedImport
        fx = fileinfo_check_tests.check_callback(
            pysourceinfo.fileinfo.getcaller_package_filepathname, 2)
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
        sys.path.insert(0, os.path.dirname(__file__) +
                        os.sep + '..' + os.sep + '..')
        sys.path.insert(0, os.path.dirname(__file__))
        import fileinfo_check_tests  # @UnresolvedImport

#         fx0 = os.path.dirname(fileinfo_check_tests.__file__) + \
#             os.sep + ".." + os.sep + ".." + os.sep + ".."
#         fx1 = os.path.dirname(fileinfo_check_tests.__file__) + os.sep + ".."
#         fx2 = os.path.dirname(fileinfo_check_tests.__file__) + \
#             os.sep + ".." + os.sep + ".."
#        fx3 = os.path.dirname(__file__)
        fx4 = __file__

        fx = fileinfo_check_tests.check_callback(
            pysourceinfo.fileinfo.getcaller_package_filepathname, 2)
        fx = os.path.normpath(fx)

#         fx0 = os.path.abspath(fx0)
#         fx1 = os.path.abspath(fx1)
#         fx2 = os.path.abspath(fx2)
#        fx3 = os.path.abspath(fx3)
        fx4 = os.path.abspath(fx4)

        fx = os.path.abspath(fx)

#         fx0 = os.path.realpath(os.path.normpath(fx0))
#         fx1 = os.path.normpath(os.path.normpath(fx1))
#         fx2 = os.path.normpath(os.path.normpath(fx2))
#        fx3 = os.path.normpath(os.path.normpath(fx3))
        fx4 = os.path.normpath(os.path.normpath(fx4))

        fx = os.path.normpath(os.path.normpath(fx))

        sys.path.pop(0)
        sys.path.pop(0)
        self.assertEqual(sys.path, _s)

#        assert fx == fx0 or fx == fx1 or fx == fx2 or fx == fx3 or fx == fx4
        assert fx == fx4[:-1] or fx == fx4  

    def testcase021(self):
        #
        # Depends on the call.
        #
        import sys
        _s = sys.path[:]
        sys.path.insert(0, os.path.dirname(__file__) +
                        os.sep + '..' + os.sep + '..')
        sys.path.insert(0, os.path.dirname(__file__) + os.sep + '..')
        import fileinfo_check_tests  # @UnresolvedImport

#         fx0 = os.path.dirname(fileinfo_check_tests.__file__) + \
#             os.sep + ".." + os.sep + ".." + os.sep + ".."
#         fx1 = os.path.dirname(fileinfo_check_tests.__file__) + os.sep + ".."
#         fx2 = os.path.dirname(fileinfo_check_tests.__file__) + \
#             os.sep + ".." + os.sep + ".."
        fx3 = os.path.dirname(__file__)
#         fx4 = __file__

        fx = fileinfo_check_tests.check_callback(
            pysourceinfo.fileinfo.getcaller_package_filepathname, 2)
        fx = os.path.normpath(fx)

#         fx0 = os.path.abspath(fx0)
#         fx1 = os.path.abspath(fx1)
#         fx2 = os.path.abspath(fx2)
        fx3 = os.path.abspath(fx3)
#         fx4 = os.path.abspath(fx4)

        fx = os.path.abspath(fx)

#         fx0 = os.path.realpath(os.path.normpath(fx0))
#         fx1 = os.path.normpath(os.path.normpath(fx1))
#         fx2 = os.path.normpath(os.path.normpath(fx2))
        fx3 = os.path.normpath(os.path.normpath(fx3))
#         fx4 = os.path.normpath(os.path.normpath(fx4))

        fx = os.path.normpath(os.path.normpath(fx))

        sys.path.pop(0)
        sys.path.pop(0)
        self.assertEqual(sys.path, _s)

#        assert fx == fx0 or fx == fx1 or fx == fx2 or fx == fx3 or fx == fx4
        assert fx == fx3

    def testcase022(self):
        #
        # Depends on the call.
        #
        import sys
        _s = sys.path[:]
        sys.path.insert(0, os.path.dirname(__file__) +
                        os.sep + '..' + os.sep + '..')
        import fileinfo_check_tests  # @UnresolvedImport

#         fx0 = os.path.dirname(fileinfo_check_tests.__file__) + \
#             os.sep + ".." + os.sep + ".." + os.sep + ".."
#         fx1 = os.path.dirname(fileinfo_check_tests.__file__) + os.sep + ".."
        fx2 = os.path.dirname(__file__) + os.sep + ".."
#        fx3 = os.path.dirname(__file__)
#         fx4 = __file__

        fx = fileinfo_check_tests.check_callback(
            pysourceinfo.fileinfo.getcaller_package_filepathname, 2)
        fx = os.path.normpath(fx)

#         fx0 = os.path.abspath(fx0)
#         fx1 = os.path.abspath(fx1)
        fx2 = os.path.abspath(fx2)
#        fx3 = os.path.abspath(fx3)
#         fx4 = os.path.abspath(fx4)

        fx = os.path.abspath(fx)

#         fx0 = os.path.realpath(os.path.normpath(fx0))
#         fx1 = os.path.normpath(os.path.normpath(fx1))
        fx2 = os.path.normpath(os.path.normpath(fx2))
#        fx3 = os.path.normpath(os.path.normpath(fx3))
#         fx4 = os.path.normpath(os.path.normpath(fx4))

        fx = os.path.normpath(os.path.normpath(fx))

        sys.path.pop(0)
        self.assertEqual(sys.path, _s)

#        assert fx == fx0 or fx == fx1 or fx == fx2 or fx == fx3 or fx == fx4
        assert fx == fx2

    def testcase030(self):
        import sys
        _s = sys.path[:]
        sys.path.insert(0, os.path.dirname(__file__) +
                        os.sep + '..' + os.sep + '..')
        import fileinfo_check_tests  # @UnresolvedImport

        fx = fileinfo_check_tests.check_callback(
            pysourceinfo.fileinfo.getcaller_package_filepathname, 3)

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
