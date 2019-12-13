from __future__ import absolute_import

import unittest
import sys
import os

import sourceinfo.infolists
from sourceinfo.objectinfo import getcaller_module
from sourceinfo.fileinfo import getmodule_pathname

#
#######################
#


class CallUnits(unittest.TestCase):
    def testcase000(self):
        cm = getcaller_module()
        #mx = sys.modules[cm]
        #mid = id(mx)

        fpn0 = getmodule_pathname(cm)
        fpn1 = sorted(sourceinfo.infolists.getsysmodules_pathname_list(
            os.path.normpath('getsysmodules_pathname_list/CallCase')))

        assert [fpn0] == fpn1


if __name__ == '__main__':
    unittest.main()
