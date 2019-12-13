from __future__ import absolute_import

import unittest
import imp

from sourceinfo.objectinfo import getcaller_module, MT_SOURCE
from sourceinfo.fileinfo import getmodule_filepathname
from sourceinfo.helper import getfilepathname_type

#
#######################
#


class CallUnits(unittest.TestCase):

    def get_moddata(self):
        cm = getcaller_module(2)
        cmf = getmodule_filepathname(cm)
        mtype = getfilepathname_type(cmf)
        return mtype

    def testcase000(self):
        import sys
        sys.dont_write_bytecode = True
        from testdata.pysourceinfo.moduletypes.python2.mronew.source.module import CModule

        callback = self.get_moddata
        cm = CModule()
        cmd = cm.getData(callback)

        assert cmd == MT_SOURCE

    def testcase001(self):
        import sys
        sys.bytecodebase = None
        from testdata.pysourceinfo.moduletypes.python2.mronew.source.module import CModule

        callback = self.get_moddata
        cm = CModule()
        cmd = cm.getData(callback)

        assert cmd == MT_SOURCE

    def testcase010(self):
        import sys
        sys.dont_write_bytecode = True
        from testdata.pysourceinfo.moduletypes.python2.mronew.source.module import CModule

        callback = self.get_moddata
        cm = CModule()
        cmd = cm.getData(callback)

        assert cmd == MT_SOURCE

    def testcase011(self):
        import sys
        sys.bytecodebase = None
        from testdata.pysourceinfo.moduletypes.python2.mronew.source.module import CModule

        callback = self.get_moddata
        cm = CModule()
        cmd = cm.getData(callback)

        assert cmd == MT_SOURCE


if __name__ == '__main__':
    unittest.main()
