from __future__ import absolute_import

import unittest
import sys

import pysourceinfo.objectinfo
import pysourceinfo.infolists


#
#######################
#
class CallUnits(unittest.TestCase):
    def testcase000(self):
        cm = pysourceinfo.objectinfo.getcaller_module_name()
        #mx = sys.modules[cm]
        #mid = id(mx)

        fpn = sorted(pysourceinfo.infolists.getsysmodules_name_list(
            'objectinfo.getmodule_name.CallCase'))

        assert cm == fpn[0]


if __name__ == '__main__':
    unittest.main()
