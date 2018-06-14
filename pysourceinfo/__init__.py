# -*- coding: utf-8 -*-
"""'pysourceinfo' - Python RTTI based on 'inspect'"""
from __future__ import absolute_import
from sys import version_info

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2017 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.21'
__uuid__ = 'efed42d3-f801-4fbb-abfd-bd598d683a82'
__docformat__ = "restructuredtext en"


class PySourceInfoError(Exception):
    """Common parent exception for the *pysourceinfo* package."""
    def __init__(self, *args, **kw):
        super(PySourceInfoError, self).__init__(*args, **kw)

V3K = False  # : Python3.5+
if version_info[:2] > (3, 4,):
    V3K = True
    _STR = (str,)  # : string and unicode
    from importlib import find_loader  # @UnresolvedImport
    vers = '{0}{1}'.format(*version_info[:2])  # pylint: disable-msg=W0142
elif version_info[:2] > (2, 6,) and version_info[:2][0] < 3:
    _STR = (str, unicode,)  # : string and unicode @UndefinedVariable
else:
    raise PySourceInfoError(
        "Requires Python 2.7+, or 3.5+:" + str(version_info[:2]))


# deprecated with 3.3/__pycache__, but still require these, going to use own values than
# re-map for smart import/export
MT_UNKNOWN = 0
MT_SOURCE = 1  #: same value as PY_SOURCE = 1
MT_COMPILED = 2  #: same value as PY_COMPILED = 2
MT_EXTENSION = 3  # : same value as C_EXTENSION = 3
MT_DIRECTORY = 5  # : same value as PKG_DIRECTORY = 5
MT_BUILTIN = 6  # : same value as C_BUILTIN = 6
MT_FROZEN = 7  # : same value as PY_FROZEN = 7

MT_COMPILED_OPT = 10  # : PY_COMPILED | <opt1 or opt2> # 2 | 8
MT_COMPILED_OPT1 = 18  # : PY_COMPILED | <opt1> # 2 | 16
MT_COMPILED_OPT2 = 34  # : PY_COMPILED | <opt2> # 2 | 32
MT_COMPILED_DEBUG = 66  # : PY_COMPILED | 0 # 2 | 64


#
# bits defining the evaluated package path 
# from PYTHONPATH in case of multiple matches
#
P_FIRST = 1  #: first matched path-prefix
P_LAST = 2  #: last matched path-prefix
P_SHORTEST= 4  #: longest matched path-prefix
P_LONGEST = 8  #: longest matched path-prefix
P_IGNORE0 = 16  #: ignores sys.path[0] - the execution path

presolve = P_FIRST  #: default value for sys.path resolution

__all__ = [
    'bininfo',
    "fileinfo.py",
    "helper.py",
    "infolists.py",
    "objectinfo.py",
]
