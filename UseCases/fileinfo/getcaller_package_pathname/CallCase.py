"""Check defaults.
"""
from __future__ import absolute_import

import unittest
import os

import pysourceinfo.fileinfo


#
#######################
#
class CallUnits(unittest.TestCase):

    def testcase002(self):
        import sys
        _s = sys.path[:]
        
        #Clear from misguided previous tests
        i=len(_s)-1
        for ix in reversed(_s):
            if ix.find('UseCases') != -1:
                sys.path.pop(i)
            i-=1
            
        sys.path.insert(0,os.path.abspath(os.path.dirname(__file__)+os.sep+'..'))
        import fileinfo_check_usecases #@UnresolvedImport

        # Adapts to behaviour of 'inspect'
        fx0 = os.path.dirname(__file__)+os.sep+".."  # this should be the actual and only and one here
        fx1 = os.path.dirname(__file__)+os.sep+".."+os.sep+".."+os.sep+".."
        fx2 = os.path.dirname(__file__)+os.sep+".."+os.sep+".."+os.sep+".."+".."+os.sep+".."
        fx = fileinfo_check_usecases.check_callback(pysourceinfo.fileinfo.getcaller_package_pathname,2)

        # for relative calls
        fx0 =os.path.abspath(fx0)
        fx1 =os.path.abspath(fx1)
        fx2 =os.path.abspath(fx2)
        fx =os.path.abspath(fx)

        fx0 = os.path.normpath(fx0)
        fx1 = os.path.normpath(fx1)
        fx = os.path.normpath(fx)

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)

        assert fx == fx0 or fx == fx1 or fx == fx2

    def testcase003(self):
        import sys
        _s = sys.path[:]
        
        #Clear from misguided previous tests
        i=len(_s)-1
        for ix in reversed(_s):
            if ix.find('UseCases') != -1:
                sys.path.pop(i)
            i-=1
            
        sys.path.insert(0,os.path.abspath(os.path.dirname(__file__)+os.sep+'..'))
        import fileinfo_check_usecases #@UnresolvedImport
        
        fx = fileinfo_check_usecases.check_callback(pysourceinfo.fileinfo.getcaller_package_pathname,3)

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)


        version = '{0}.{1}'.format(*sys.version_info[:2])
        
        assert os.path.exists(fx + os.sep + 'unittest')

if __name__ == '__main__':
    unittest.main()
