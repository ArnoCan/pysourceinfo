from __future__ import absolute_import

import unittest
import os
import sys

import sourceinfo.infolists
from sourceinfo import P_LONGEST


#
#######################
#
class CallUnits(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        sys.path.insert(
            0, 
            os.path.abspath(os.path.normpath(os.path.dirname(__file__) + os.sep + '..'))
            )

    def testcase000(self):
        # cm = sourceinfo.objectinfo.getcaller_module()
        # px = sourceinfo.helper.getpythonpath('getmodules_pythonpath_list/CallCase.py', presolve=P_LONGEST)
        ppn = sourceinfo.infolists.getsysmodules_python_pathname_list(
            'getmodules_pythonpath_list/CallCase',
            presolve=P_LONGEST            
            )

        self.assertTrue(ppn[0] in sys.path)
        self.assertTrue(os.path.abspath(__file__).startswith(ppn[0]))


if __name__ == '__main__':
    unittest.main()
