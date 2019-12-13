from __future__ import absolute_import

import unittest
import imp

from pythonids.pythondist import PYDIST, PYE_DIST, PYE_JYTHON

from pythonids import PYV35Plus, PYV38, PYVxyz
from sourceinfo import \
    MT_SOURCE, MT_COMPILED, MT_FROZEN, \
    MT_COMPILED_OPT1, MT_COMPILED_OPT2, MT_COMPILED_DEBUG
from sourceinfo.objectinfo import getcaller_module, MT_SOURCE, MT_BUILTIN, getmodule_type, getmodule_oid
from sourceinfo.fileinfo import getmodule_filepathname
from sourceinfo.helper import getfilepathname_type

#
#######################
#


class CallUnits(unittest.TestCase):

    def testcase000(self):
        import zipimport
        mtype = getmodule_type(zipimport)
        if PYVxyz >= PYV38:
            assert mtype in (MT_SOURCE, MT_FROZEN)
        else:
            assert mtype in (MT_SOURCE, MT_BUILTIN)

    def testcase010(self):
        mtype = getmodule_type(imp)

        if PYDIST & PYE_DIST == PYE_JYTHON:
            # original value by jython
            assert mtype in (MT_SOURCE,)
            
        else:
            if PYV35Plus:
                assert mtype in (MT_SOURCE, MT_COMPILED_OPT1, MT_COMPILED_OPT2, MT_COMPILED_DEBUG)
            else:
                assert mtype in (MT_BUILTIN,)


if __name__ == '__main__':
    unittest.main()
