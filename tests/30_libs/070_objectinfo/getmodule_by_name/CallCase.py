from __future__ import absolute_import

import unittest
import os

from pysourceinfo.objectinfo import getcaller_module_name, getmodule_by_name

#
#######################
#


class CallUnits(unittest.TestCase):
    def testcase000(self):
        import sys
        cm = getcaller_module_name()
        mx = sys.modules[cm]

        mn = getmodule_by_name(cm)

        assert mn == mx


if __name__ == '__main__':
    unittest.main()
