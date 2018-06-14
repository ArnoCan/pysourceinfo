from __future__ import absolute_import
from __future__ import print_function

import unittest

import pysourceinfo.infolists
from pysourceinfo.objectinfo import getcaller_module_name

#
#######################
#


class CallUnits(unittest.TestCase):
    def testcase000(self):
        cm = getcaller_module_name()

        # tests
        # tests.30_libs
        # tests.30_libs.050_infolists
        # tests.30_libs.050_infolists.getsysmodules_name_list
        # tests.30_libs.050_infolists.getsysmodules_name_list.CallCase
        fpn = sorted(pysourceinfo.infolists.getsysmodules_name_list(
            'getsysmodules_name_list.CallCase'))

        assert [cm] == fpn


if __name__ == '__main__':
    unittest.main()
