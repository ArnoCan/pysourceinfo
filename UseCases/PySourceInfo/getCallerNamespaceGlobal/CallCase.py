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
    def testCase000(self):
        import sys
        _sx = repr(sys.path)
        sys.path.insert(0,os.path.abspath(os.path.dirname(__file__)+os.sep+'..'))
        import PySourceInfo_check #@UnresolvedImport
        
        fx = PySourceInfo_check.check_callback(pysourceinfo.PySourceInfo.getCallerNamespaceGlobal,0)
        fx = fx['__name__']
        
        assert fx == 'pysourceinfo.PySourceInfo'
        assert _sx != repr(sys.path)
        sys.path.pop(0)
        assert _sx == repr(sys.path)

    def testCase001(self):
        import sys
        _sx = repr(sys.path)
        sys.path.insert(0,os.path.abspath(os.path.dirname(__file__)+os.sep+'..'))
        import PySourceInfo_check #@UnresolvedImport
        
        fx = PySourceInfo_check.check_callback(pysourceinfo.PySourceInfo.getCallerNamespaceGlobal,1)
        fx = fx['__name__']

        assert fx == 'PySourceInfo_check'
        assert _sx != repr(sys.path)
        sys.path.pop(0)
        assert _sx == repr(sys.path)

    def testCase002(self):
        import sys
        _sx = repr(sys.path)
        sys.path.insert(0,os.path.abspath(os.path.dirname(__file__)+os.sep+'..'))
        import PySourceInfo_check #@UnresolvedImport
        
        fx0 = 'UseCases.PySourceInfo.getCallerNamespaceGlobal.CallCase'
        fx1 = 'PySourceInfo.getCallerNamespaceGlobal.CallCase'
        fx = PySourceInfo_check.check_callback(pysourceinfo.PySourceInfo.getCallerNamespaceGlobal,2)
        fx = fx['__name__']

        assert fx == fx0 or fx == fx1
        assert _sx != repr(sys.path)
        sys.path.pop(0)
        assert _sx == repr(sys.path)

    def testCase003(self):
        import sys
        _sx = repr(sys.path)
        sys.path.insert(0,os.path.abspath(os.path.dirname(__file__)+os.sep+'..'))
        import PySourceInfo_check #@UnresolvedImport
        
        fx = PySourceInfo_check.check_callback(pysourceinfo.PySourceInfo.getCallerNamespaceGlobal,3)
        fx = fx['__name__']
        
        version = '{0}.{1}'.format(*sys.version_info[:2])
        if version == '2.6': # pragma: no cover
            assert fx == 'unittest'
        elif version == '2.7': # pragma: no cover
            assert fx == 'unittest.case'
        else:
            assert False
        assert _sx != repr(sys.path)
        sys.path.pop(0)
        assert _sx == repr(sys.path)
        
if __name__ == '__main__':
    unittest.main()
