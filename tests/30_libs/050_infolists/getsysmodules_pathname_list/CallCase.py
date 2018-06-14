from __future__ import absolute_import

import unittest
import sys
import os

import pysourceinfo.infolists
from pysourceinfo.objectinfo import getcaller_module
from pysourceinfo.fileinfo import getmodule_pathname

#
#######################
#


class CallUnits(unittest.TestCase):
    def testcase000(self):
        cm = getcaller_module()
        #mx = sys.modules[cm]
        #mid = id(mx)

        fpn0 = getmodule_pathname(cm)
        fpn1 = sorted(pysourceinfo.infolists.getsysmodules_pathname_list(
            os.path.normpath('getsysmodules_pathname_list/CallCase')))

        assert [fpn0] == fpn1


if __name__ == '__main__':
    unittest.main()
