from __future__ import absolute_import

import unittest
import imp

from pysourceinfo import V3K, \
    MT_SOURCE, MT_COMPILED, \
    MT_COMPILED_OPT1, MT_COMPILED_OPT2, MT_COMPILED_DEBUG
from pysourceinfo.objectinfo import getcaller_module, MT_SOURCE, MT_BUILTIN, getmodule_type
from pysourceinfo.fileinfo import getmodule_filepathname
from pysourceinfo.helper import getfilepathname_type

#
#######################
#


class CallUnits(unittest.TestCase):

    def testcase000(self):
        import zipimport
        mtype = getmodule_type(zipimport)

        assert mtype in (MT_SOURCE, MT_BUILTIN)

    def testcase010(self):
        mtype = getmodule_type(imp)

        if V3K:
            assert mtype in (MT_SOURCE, MT_COMPILED_OPT1, MT_COMPILED_OPT2, MT_COMPILED_DEBUG)
        else:
            assert mtype in (MT_BUILTIN,)


if __name__ == '__main__':
    unittest.main()
