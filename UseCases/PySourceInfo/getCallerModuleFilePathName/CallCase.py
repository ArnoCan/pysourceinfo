"""Check defaults.
"""
from __future__ import absolute_import

import unittest
import os

import pysourceinfo.PySourceInfo


#
#######################
#
class CallUnits(unittest.TestCase):

    def testCase003(self):
        import sys
        _sx = repr(sys.path)
        sys.path.insert(0,os.path.abspath(os.path.dirname(__file__)+os.sep+'..'))
        import PySourceInfo_check #@UnresolvedImport
        
        fx = PySourceInfo_check.check_callback(pysourceinfo.PySourceInfo.getCallerModuleFilePathName,3)

        version = '{0}.{1}'.format(*sys.version_info[:2])
        if version == '2.6': # pragma: no cover
            assert os.path.basename(fx) == 'unittest.py'
        elif version == '2.7': # pragma: no cover
            assert os.path.basename(fx) == 'case.py'
        else:
            assert False

        assert _sx != repr(sys.path)
        sys.path.pop(0)
        assert _sx == repr(sys.path)

if __name__ == '__main__':
    unittest.main()
