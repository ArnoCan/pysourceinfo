from __future__ import absolute_import
from __future__ import print_function

import unittest

import sourceinfo.infolists
from sourceinfo.objectinfo import getcaller_module_name

#
#######################
#


class CallUnits(unittest.TestCase):
    def testcase000(self):
        cm = getcaller_module_name()

        # tests
        # tests.lib
        # tests.libs.infolists
        # tests.libs.infolists.getsysmodules_name_list
        # tests.libs.infolists.getsysmodules_name_list.CallCase
        fpn = sorted(sourceinfo.infolists.getsysmodules_name_list(
            'getsysmodules_name_list.CallCase'))

        assert [cm] == fpn


if __name__ == '__main__':
    unittest.main()
