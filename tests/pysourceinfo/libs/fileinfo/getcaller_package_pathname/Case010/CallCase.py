"""Check defaults.
"""
from __future__ import absolute_import

import unittest
import os
import sys

import sourceinfo.fileinfo
import testdata.pysourceinfo
import tests

#
#######################
#
class CallUnits(unittest.TestCase):
    def testcase000(self):
        ppn = sourceinfo.fileinfo.getcaller_package_pathname()
        sys.path.insert(0, testdata.pysourceinfo.mypath)
        fpn = sourceinfo.fileinfo.getcaller_pathname_sub()
        p = os.path.dirname(os.path.abspath(tests.__file__)) + os.path.sep + fpn
        f = os.path.dirname(os.path.abspath(__file__))
        
        #
        # 4TEST:
        #
#         print("4TEST:")        
#         print("4TEST:")        
#         print("4TEST:ppn = " + str(ppn))
#         print("4TEST:fpn = " + str(fpn))
#         print("4TEST:p   = " + str(p))
#         print("4TEST:f   = " + str(f)) 
#         print("4TEST:")        
#         print("4TEST:")        
       
        self.assertEqual(p, f)


if __name__ == '__main__':
    unittest.main()
