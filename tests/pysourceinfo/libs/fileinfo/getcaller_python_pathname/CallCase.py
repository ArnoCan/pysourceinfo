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
    def testcase000(self):
        import sys
        _s = sys.path[:]
        _sx = repr(sys.path)
        sys.path.insert(0, os.path.normpath(
            os.path.dirname(__file__) + os.sep + '..'))
        sys.path.insert(0, os.path.normpath(os.path.dirname(__file__)))

        ppn = sourceinfo.fileinfo.getcaller_python_pathname()
        fpn = sourceinfo.fileinfo.getcaller_pathname_rel()

        pn = os.path.normpath(ppn + os.path.sep + fpn)
         
        assert _sx != repr(sys.path)
        sys.path.pop(0)
        sys.path.pop(0)
        assert _sx == repr(sys.path)

        assert pn == os.path.dirname(os.path.abspath(__file__))

    def testcase010(self):
        import sys
        _s = sys.path[:]
        _sx = repr(sys.path)
        sys.path.insert(0, os.path.normpath(
            os.path.dirname(__file__) + os.sep + '..' ))
        sys.path.insert(0, os.path.normpath(os.path.dirname(__file__) + os.sep + '..'))

        ppn = sourceinfo.fileinfo.getcaller_python_pathname()
        fpn = sourceinfo.fileinfo.getcaller_pathname_rel()

        pn = os.path.normpath(ppn + os.path.sep + fpn)
         
        assert _sx != repr(sys.path)
        sys.path.pop(0)
        sys.path.pop(0)
        assert _sx == repr(sys.path)

        assert pn == os.path.dirname(os.path.abspath(__file__))

    def testcase20(self):
        import sys
        _s = sys.path[:]
        _sx = repr(sys.path)
        sys.path.insert(0, os.path.normpath(
            os.path.dirname(__file__) + os.sep))
        sys.path.insert(0, os.path.normpath(os.path.dirname(__file__) + '..' + os.sep + '..' + os.sep + '..'))

        ppn = sourceinfo.fileinfo.getcaller_python_pathname()
        fpn = sourceinfo.fileinfo.getcaller_pathname_rel()

        pn = os.path.normpath(ppn + os.path.sep + fpn)
         
        assert _sx != repr(sys.path)
        sys.path.pop(0)
        sys.path.pop(0)
        assert _sx == repr(sys.path)

        assert pn == os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':
    unittest.main()
