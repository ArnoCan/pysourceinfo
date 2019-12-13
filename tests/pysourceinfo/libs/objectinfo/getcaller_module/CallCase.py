"""Check defaults.
"""
from __future__ import absolute_import

import unittest
import os

import sourceinfo.objectinfo


#
#######################
#
class CallUnits(unittest.TestCase):
    def testcase000(self):

        fx = sourceinfo.objectinfo.getcaller_module()
        self.assertEqual(os.path.normpath(fx.__name__),
                         'tests.pysourceinfo.libs.objectinfo.getcaller_module.CallCase')
        pass


if __name__ == '__main__':
    unittest.main()
