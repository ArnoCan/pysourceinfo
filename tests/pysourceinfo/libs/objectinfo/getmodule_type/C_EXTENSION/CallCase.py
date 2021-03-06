from __future__ import absolute_import

import unittest
import os
import imp

from sourceinfo import \
    MT_SOURCE, MT_COMPILED, \
    MT_COMPILED_OPT1, MT_COMPILED_OPT2, MT_COMPILED_DEBUG
from sourceinfo.objectinfo import getcaller_module, getmodule_type
from sourceinfo.fileinfo import getmodule_filepathname
from sourceinfo.helper import getfilepathname_type


#
#######################
#
class CallUnits(unittest.TestCase):
    def testcase000(self):
        cm = getcaller_module()
        mtype = getmodule_type(cm)

        assert mtype in (MT_SOURCE, MT_COMPILED, MT_COMPILED_OPT1, MT_COMPILED_OPT2, MT_COMPILED_DEBUG)


if __name__ == '__main__':
    unittest.main()
