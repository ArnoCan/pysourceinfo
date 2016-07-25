"""Check defaults.
"""
from __future__ import absolute_import

import unittest
import os

from pysourceinfo.PySourceInfo import getStackFuncNameMap,getStackLen,getCallerFunc


#
#######################
#
class CallUnits(unittest.TestCase):

    def callFunc(self,cfunc,param):
        """Function dummy, traces current stack by two different calls, normalizes the calls. 
        """
        return cfunc(param)

    def wrapStackDepth(self,deepness,cfunc,param):
        """Simulates depth of callstack.
        """
        if deepness > 0:
            _r = self.wrapStackDepth(deepness-1, cfunc, param)
        else:
            return self.callFunc(cfunc,param)
        return _r

    def testCase000(self):
        """simple upper call stack
        """
        c = self.wrapStackDepth(4, getStackFuncNameMap,'testCase000')
        assert c[7] == 'testCase000'
        pass

    def testCase001(self):
        """simple upper call stack
        """
        c = self.wrapStackDepth(4, getStackFuncNameMap,'wrapStackDepth')
        self.assertEqual( c, {
                2: 'wrapStackDepth',
                3: 'wrapStackDepth',
                4: 'wrapStackDepth',
                5: 'wrapStackDepth',
                6: 'wrapStackDepth',
            }
        )
        pass

if __name__ == '__main__':
    unittest.main()
