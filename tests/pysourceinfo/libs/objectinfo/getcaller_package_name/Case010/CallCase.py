"""Check defaults.
"""
from __future__ import absolute_import

import unittest
import os

from sourceinfo.objectinfo import getcaller_package_name

#
#######################
#


class CallUnits(unittest.TestCase):
    def testcase000(self):
        fpn = getcaller_package_name()
        assert fpn == 'tests'


if __name__ == '__main__':
    unittest.main()
