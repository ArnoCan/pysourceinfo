from __future__ import absolute_import

import unittest
import os
import sys
import re

import pysourceinfo.infolists


#
#######################
#
class CallUnits(unittest.TestCase):
    def testcase000(self):
        fpn = sorted(pysourceinfo.infolists.getsysmodules_filepathname_list(
            os.path.normpath('getmodule_filepathname_list/CallCase')))            
        spn = os.path.abspath(__file__)
        assert fpn[0] == spn


if __name__ == '__main__':
    unittest.main()
