from __future__ import absolute_import

import unittest
import sys

import sourceinfo.objectinfo
import sourceinfo.infolists


#
#######################
#
class CallUnits(unittest.TestCase):
    def testcase000(self):
        cm = sourceinfo.objectinfo.getcaller_module_name()
        #mx = sys.modules[cm]
        #mid = id(mx)

        fpn = sorted(sourceinfo.infolists.getsysmodules_name_list(
            'objectinfo.getmodule_name.CallCase'))

        assert cm == fpn[0]


if __name__ == '__main__':
    unittest.main()
