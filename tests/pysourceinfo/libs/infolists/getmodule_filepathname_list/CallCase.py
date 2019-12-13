from __future__ import absolute_import

import unittest
import os
import sys

import sourceinfo.infolists
from sourceinfo import P_LONGEST


# from rdbg.start import start_remote_debug    # load a slim bootstrap module for stage-0
# start_remote_debug()                         # check whether '--rdbg' option is present, if so accomplish bootstrap


class CallUnits(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        
        sys.path.insert(
            0, 
            os.path.abspath(os.path.normpath(os.path.dirname(__file__) + os.sep + '..'))
            )

    def tearDown(self):
        unittest.TestCase.tearDown(self)
        sys.path.pop(0)

    def testcase000(self):
        """relative path
        """
        fpn_lst = sourceinfo.infolists.getsysmodules_filepathname_list(
                os.path.normpath('getmodule_filepathname_list/CallCase')
            )
        fpn = sorted(fpn_lst)            
        spn = __file__
        self.assertEqual(fpn[0], spn)


    def testcase010(self):
        """absolute path
        """
        debugdummy = sys.path  # @UnusedVariable
        p = 'getmodule_filepathname_list/CallCase'
        l = sourceinfo.infolists.getsysmodules_filepathname_list(p, abs=True, presolve=P_LONGEST)
        fpn = sorted(l)
        spn = os.path.abspath(__file__)
        self.assertEqual(fpn[0], spn)

if __name__ == '__main__':
    unittest.main()
