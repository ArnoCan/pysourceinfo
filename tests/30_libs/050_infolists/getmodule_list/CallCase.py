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
        mx = sys.modules[cm]
        #mid = id(mx)

        fpn = sorted(pysourceinfo.infolists.getsysmodules_list(
            'tests.30_libs.050_infolists.getmodule_list.CallCase'))

        assert [mx] == fpn


if __name__ == '__main__':
    unittest.main()
