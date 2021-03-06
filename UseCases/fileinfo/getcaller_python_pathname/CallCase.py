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

    def testcase002(self):
        import sys
        _s=sys.path[:]

        #Clear from misguided previous tests
        i=len(_s)-1
        for ix in reversed(_s):
            if ix.find('UseCases') != -1:
                sys.path.pop(i)
            i-=1

        sys.path.insert(0,os.path.abspath(os.path.dirname(__file__)+os.sep+'..'))
        import fileinfo_check_usecases #@UnresolvedImport
        
        fx0 = os.path.normpath(os.path.dirname(__file__))
        fx1 = os.path.dirname(fileinfo_check_usecases.__file__)
        fx2 = os.path.dirname(fileinfo_check_usecases.__file__)+os.sep+'..'
        fx3 = os.path.dirname(fileinfo_check_usecases.__file__)+os.sep+'..'+os.sep+'..'
        fx = fileinfo_check_usecases.check_callback(sourceinfo.fileinfo.getcaller_python_pathname,2)

        # for relative calls
        fx0 =os.path.abspath(fx0)
        fx1 =os.path.abspath(fx1)
        fx2 =os.path.abspath(fx2)
        fx3 =os.path.abspath(fx3)
        fx =os.path.abspath(fx)

        fx0 = os.path.normpath(fx0)
        fx1 = os.path.normpath(fx1)
        fx2 = os.path.normpath(fx2)
        fx3 = os.path.normpath(fx3)
        fx = os.path.normpath(fx)

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)

        assert fx == fx0 or fx == fx1 or fx == fx2 or fx == fx3

if __name__ == '__main__':
    unittest.main()
