from __future__ import absolute_import

import unittest
import os
import sys
import imp

from sourceinfo.objectinfo import getmodule_package_name, getcaller_module, getmodule_type
from sourceinfo.objectinfo import MT_SOURCE, MT_DIRECTORY
from sourceinfo.objectinfo import getmodule_name


s = os.path.sep

#
#######################
#


class CallUnits(unittest.TestCase):

    def testcase000(self):
        import testdata.pysourceinfo.packages.python2.package as testdata_pkg
        cm0 = getmodule_name(testdata_pkg)
        import testdata.pysourceinfo
        sys.path.insert(0, testdata.pysourceinfo.mypathname + s +
                        "packages" + s + "python2")
        import package  # @UnresolvedImport
        cm1 = getmodule_name(package)
        assert "package" == cm1

    def testcase010(self):
        """package name is the relative path"""
        import testdata.pysourceinfo.packages.python2.package as testdata_pkg
        cm = getmodule_name(testdata_pkg)
        assert 'package' == cm
        cpm = getmodule_package_name(testdata_pkg)
        assert 'testdata.pysourceinfo.packages.python2.package' == cpm
        pass

    def testcase020(self):
        """package name is the the sub-directory of the package only"""
        import testdata.pysourceinfo
        sys.path.insert(0, testdata.pysourceinfo.mypathname + s +
                        "packages" + s + "python2")
        import package  # @UnresolvedImport
        cm = getmodule_name(package)
        assert 'package' == cm
        cpm = getmodule_package_name(package)
        assert 'package' == cpm
        pass

    def testcase030(self):
        """package name is the the sub-directory of the package only"""
        import testdata.pysourceinfo
        sys.path.insert(0, testdata.pysourceinfo.mypathname + s +
                        "packages" + s + "python2")
        import package  # @UnresolvedImport
        cm = getmodule_name(package)
        assert 'package' == cm
        cpm = getmodule_package_name(package)
        assert 'package' == cpm
        sys.path.pop(0)
        sys.path.insert(0, testdata.pysourceinfo.mypathname + s + "packages")
        cm = getmodule_name(package)
        assert 'package' == cm
        cpm = getmodule_package_name(package)
        assert 'package' == cpm
        pass

    def testcase100(self):
        cm = getcaller_module()
        mpn = getmodule_package_name(cm)
        assert mpn == "tests.pysourceinfo.libs.objectinfo.getmodule_package_name.CallCase"


if __name__ == '__main__':
    unittest.main()
