from __future__ import absolute_import

import unittest
import os

from pysourceinfo.objectinfo import getcaller_module_name, getmodule_by_id

#
#######################
#


class CallUnits(unittest.TestCase):
    def testcase000(self):
        import sys
        cm = getcaller_module_name()
        mx = sys.modules[cm]
        mid = id(mx)

        fpn = getmodule_by_id(mid)
        assert mx == fpn


if __name__ == '__main__':
    unittest.main()
