from __future__ import absolute_import

import unittest

from pysourceinfo.fileinfo import getmodule_filepathname
from pysourceinfo.objectinfo import getcaller_module
from pysourceinfo.objectinfo import MT_SOURCE, MT_COMPILED
from pysourceinfo.helper import getfilepathname_type

#
#######################
#
class CallUnits(unittest.TestCase):

    def get_moddataSrc(self):
        cm = getcaller_module(2)
        cmf = getmodule_filepathname(cm)
        mtype = getfilepathname_type(cmf)
        return mtype

    def get_moddataCmp(self):
        cm = getcaller_module(2)
        cmf = getmodule_filepathname(cm)
        mtype = getfilepathname_type(cmf)
        return mtype

    def testcase000(self):
        import sys
        import os
        from testdata import mypathname

        s = os.path.sep
        px = mypathname + s + 'moduletypes' + s + 'python2' + s + 'mronew'
        sys.path.insert(0, px)
        import pkg.module0  # @UnresolvedImport
        callback = self.get_moddataSrc
        cm = pkg.module0.CModule0()
        cmd = cm.getData(callback)

        assert cmd == MT_SOURCE

    def testcase020(self):
        from testdata.moduletypes.python2.mronew.pkg import module1

        callback = self.get_moddataCmp
        cm = module1.CModule1()
        cmd = cm.getData(callback)

        self.skipTest("Tesdata requires platform independen compiler for Python2 + Python3")
        # assert cmd == MT_COMPILED


if __name__ == '__main__':
    unittest.main()
