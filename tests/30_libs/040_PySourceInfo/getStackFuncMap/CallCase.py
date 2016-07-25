"""Check defaults.
"""
from __future__ import absolute_import

import unittest
import os

from pysourceinfo.PySourceInfo import getStackFuncMap,getStackLen,getCallerFunc


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
        c = self.wrapStackDepth(4, getStackFuncMap,self.testCase000)
        assert c[7] == self.testCase000
        pass

    def testCase001(self):
        """simple upper call stack
        """
        c = self.wrapStackDepth(4, getStackFuncMap,self.wrapStackDepth)
        self.assertEqual( c, {
                2: self.wrapStackDepth,
                3: self.wrapStackDepth,
                4: self.wrapStackDepth,
                5: self.wrapStackDepth,
                6: self.wrapStackDepth,
            }
        )
        pass

if __name__ == '__main__':
    unittest.main()
