"""Check defaults.
"""
from __future__ import absolute_import

import unittest
import os

import pysourceinfo.objectinfo


#
#######################
#
class CallUnits(unittest.TestCase):
    def testcase000(self):

        fx = pysourceinfo.objectinfo.getcaller_module()
        self.assertEqual(os.path.normpath(fx.__name__),
                         'tests.30_libs.070_objectinfo.getcaller_module.CallCase')
        pass


if __name__ == '__main__':
    unittest.main()
