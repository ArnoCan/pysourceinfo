"""Check defaults.
"""
from __future__ import absolute_import

import unittest
import os

from pysourceinfo.PySourceInfo import getStackFuncNameList


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
        
        assert cRef == c[0:8]
        pass

    def testCase001(self):

        c = self.wrapStackDepth(4, getStackFuncNameList,True)
        cRef =  [
            'testCase001',
            'wrapStackDepth', 
            'wrapStackDepth', 
            'wrapStackDepth', 
            'wrapStackDepth', 
            'wrapStackDepth', 
            'callFunc', 
            'getStackFuncNameList', 
        ]
        
        assert cRef == c[-8:]
        pass

if __name__ == '__main__':
    unittest.main()
