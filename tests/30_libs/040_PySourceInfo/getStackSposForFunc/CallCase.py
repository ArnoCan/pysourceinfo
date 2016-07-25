"""Check defaults.
"""
from __future__ import absolute_import

import unittest
import os

from pysourceinfo.PySourceInfo import getStackSposForFunc,getStackFuncList


#
#######################
#
class CallUnits(unittest.TestCase):

    def callFunc(self,cfunc,param):
        return cfunc(param)

    def wrapStackDepth(self,deepness,cfunc,param):
        if deepness > 0:
            _r = self.wrapStackDepth(deepness-1, cfunc, param)
        else:
            return self.callFunc(cfunc,param)
        return _r

    def testCase000(self):
        """verify function - class method - reference on stack
        
        do it here indirect  due to type difference of function and method 
        """
        c = self.wrapStackDepth(4, getStackFuncList,False)
        
        mname = self.testCase000.__name__

        import inspect
        c7fi = inspect.getframeinfo(c[7])

        fname = c7fi[2] 

        a0 = id(c[7]) #@UnusedVariable
        a1 = id(self.testCase000) #@UnusedVariable
        
        ci = self.wrapStackDepth(4, getStackSposForFunc,c[7])

        assert fname == mname
        assert ci == 7
        pass

if __name__ == '__main__':
    unittest.main()
