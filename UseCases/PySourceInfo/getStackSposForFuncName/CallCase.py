"""Check defaults.
"""
from __future__ import absolute_import

import unittest
import os

from pysourceinfo.PySourceInfo import getStackSposForFuncName,getStackFuncNameList


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

        c = self.wrapStackDepth(4, getStackFuncNameList,False)
        cRef =  [
            'getStackFuncNameList', 
            'callFunc', 
            'wrapStackDepth', 
            'wrapStackDepth', 
            'wrapStackDepth', 
            'wrapStackDepth', 
            'wrapStackDepth', 
            'testCase000',
        ]

        assert c[7] == cRef[7]

        ci = self.wrapStackDepth(4, getStackSposForFuncName,c[7])
        assert ci == 7
        pass

if __name__ == '__main__':
    unittest.main()
