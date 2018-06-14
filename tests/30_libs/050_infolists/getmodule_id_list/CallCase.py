from __future__ import absolute_import

import unittest
import sys

import pysourceinfo.infolists
from pysourceinfo.objectinfo import getcaller_module_name


#
#######################
#
class CallUnits(unittest.TestCase):
    def testcase000(self):
        cm = getcaller_module_name()
        mx = sys.modules[cm]
        mid = id(mx)

        fpn = sorted(pysourceinfo.infolists.getsysmodules_id_list(mid))

        assert [mid] == fpn


if __name__ == '__main__':
    unittest.main()
