"""Check defaults.
"""
from __future__ import absolute_import

import unittest
import os

import sourceinfo.fileinfo


#
#######################
#
class CallUnits(unittest.TestCase):

    def testcase003(self):
        import sys
        _sx = repr(sys.path)
        sys.path.insert(0,os.path.abspath(os.path.dirname(__file__)+os.sep+'..'))
        import fileinfo_check_usecases #@UnresolvedImport
        
        fx = fileinfo_check_usecases.check_callback(sourceinfo.fileinfo.getcaller_filepathname,3)
        assert os.path.basename(fx) == 'case.py'
            
        assert _sx != repr(sys.path)
        sys.path.pop(0)
        assert _sx == repr(sys.path)

if __name__ == '__main__':
    unittest.main()
