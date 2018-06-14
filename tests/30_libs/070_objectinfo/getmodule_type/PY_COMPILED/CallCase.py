from __future__ import absolute_import

import unittest

from pysourceinfo.objectinfo import getcaller_module, getmodule_type
from pysourceinfo.objectinfo import MT_SOURCE, MT_COMPILED, \
    MT_COMPILED_OPT1, MT_COMPILED_OPT2, MT_COMPILED_DEBUG

#
#######################
#


class CallUnits(unittest.TestCase):

    def get_moddata(self):
        cm = getcaller_module(2)
        mtype = getmodule_type(cm)
        return mtype

    def testcase000(self):
        from testdata.moduletypes.python2.mronew.source.module import CModule

        callback = self.get_moddata
        cm = CModule()
        cmd = cm.getData(callback)

        assert cmd in (MT_SOURCE, MT_COMPILED_OPT1, MT_COMPILED_OPT2, MT_COMPILED_DEBUG)

    def testcase001(self):
        from testdata.moduletypes.python2.mronew.source.module import CModule

        callback = self.get_moddata
        cm = CModule()
        cmd = cm.getData(callback)

        self.skipTest("Tesdata requires platform independen compiler for Python2 + Python3")
        # assert cmd == MT_COMPILED

    def testcase002(self):
        from testdata.moduletypes.python2.mronew.source.module import CModule

        callback = self.get_moddata
        cm = CModule()
        cmd = cm.getData(callback)

        self.skipTest("Tesdata requires platform independen compiler for Python2 + Python3")
        # assert cmd == MT_COMPILED


if __name__ == '__main__':
    unittest.main()
