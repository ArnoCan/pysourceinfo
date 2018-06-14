from __future__ import absolute_import

import unittest
import os

import pysourceinfo.infolists
import pysourceinfo.fileinfo
import pysourceinfo.objectinfo


#
#######################
#
class CallUnits(unittest.TestCase):
    def testcase000(self):
        cm = pysourceinfo.objectinfo.getcaller_module()

        ppn = pysourceinfo.infolists.getsysmodules_python_pathname_list('CallCase')[
            0]
        rpn = pysourceinfo.fileinfo.getcaller_pathname_rel()

        a = ppn + os.path.sep + rpn
        b = os.path.abspath(os.path.dirname(__file__))

        assert a == b


if __name__ == '__main__':
    unittest.main()
