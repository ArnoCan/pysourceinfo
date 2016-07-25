"""Check defaults.
"""
from __future__ import absolute_import

import unittest
import os

from pysourceinfo.PySourceInfo import getStackFuncList, getCallerFunc,getStackLen


#
#######################
#
class CallUnits(unittest.TestCase):

    def callFunc(self,cfunc,param):
        """Function dummy, traces current stack by two different calls, normalizes the calls. 
        """
        cx = cfunc(param)
        cxRef = []
        if not param:
            for i in range(getStackLen()):
                cxRef.append(getCallerFunc(i))
        
            #adapt to different call context
            cx.pop(0)
            cxRef.pop(0)

        else:
            for i in range(getStackLen()):
                cxRef.append(getCallerFunc(i))

            #adapt to different call context
            cx.pop()
            cxRef.pop(0)
            cxRef = [x for x in reversed(cxRef)]
        ret = (cx,cxRef,)
        return ret

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
        c = self.wrapStackDepth(4, getStackFuncList,False)
        c0ID = map(id,c[0]) #@UnusedVariable
        c1ID = map(id,c[1]) #@UnusedVariable
        assert c[0] == c[1]
        pass

    def testCase001(self):
        """reversed simple upper call stack
        """
        c = self.wrapStackDepth(4, getStackFuncList,True)
        c0ID = map(id,c[0]) #@UnusedVariable
        c1ID = map(id,c[1]) #@UnusedVariable
        self.assertEqual(c[0], c[1])
        pass

    def testCase002(self):
        """both previous for eventual debugging
        """
        c = self.wrapStackDepth(4, getStackFuncList,False)
        c0ID = map(id,c[0]) #@UnusedVariable
        c1ID = map(id,c[1]) #@UnusedVariable

        d = self.wrapStackDepth(4, getStackFuncList,True)
        d0ID = map(id,d[0]) #@UnusedVariable
        d1ID = map(id,d[1]) #@UnusedVariable

        self.assertEqual(c[0], c[1])
        self.assertEqual(d[0], d[1])
        pass
if __name__ == '__main__':
    unittest.main()
