# -*- coding: utf-8 -*-
"""pysourceinfo.helper - miscellaneous utilities.

Details see @local-manuals or @[https://pythonhosted.org/pysourceinfo/]
"""
from __future__ import absolute_import
from __future__ import print_function

import os
import sys
import re
from inspect import stack
from imp import PY_SOURCE, PY_COMPILED, C_EXTENSION, PKG_DIRECTORY, C_BUILTIN, PY_FROZEN

from pysourceinfo import V3K
from pysourceinfo import PySourceInfoError
from pysourceinfo import presolve, P_FIRST, P_LAST, P_LONGEST, P_SHORTEST, P_IGNORE0

if V3K:
    # pylint: disable-msg=F0401
    from importlib.machinery import SOURCE_SUFFIXES, DEBUG_BYTECODE_SUFFIXES, OPTIMIZED_BYTECODE_SUFFIXES, BYTECODE_SUFFIXES, EXTENSION_SUFFIXES  # @UnresolvedImport
    from importlib import util  # @UnresolvedImport
    # pylint: enable-msg=F0401
else:
    from inspect import getmoduleinfo  # @UnresolvedImport


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2017 Arno-Can Uestuensoez" \
    " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.21'
__uuid__ = '9de52399-7752-4633-9fdc-66c87a9200b8'

__docformat__ = "restructuredtext en"


# redundant for dependency reduction - keep in sync with pysourceinfo.objectinfo
__MT_UNKNOWN = 0
__MT_SOURCE = 1  # PY_SOURCE #1
__MT_COMPILED = 2  # PY_COMPILED #2
__MT_EXTENSION = 3  # C_EXTENSION #3
__MT_DIRECTORY = 5  # PKG_DIRECTORY #5
__MT_BUILTIN = 6  # C_BUILTIN #6
__MT_FROZEN = 7  # PY_FROZEN #7
__MT_COMPILED_OPT1 = 10  # PY_COMPILED | <opt1> # 2 | 8
__MT_COMPILED_OPT2 = 18  # PY_COMPILED | <opt2> # 2 | 16
__MT_COMPILED_DEBUG = 34  # PY_COMPILED # 2


_scname = re.compile(
    r'''.*[\\\\/]([^.]+)[.]([^-]+)-([0-9]{2})[.](opt-[012])*([.].+)$''')


def getfilepathname_type(fpath):
    """Type for stored module as defined by *imp*."""

    if not V3K:  # for now the more frequent call
        if not os.path.exists(fpath):
            return
        ret = getmoduleinfo(fpath)
        if ret and ret[3] in (PY_SOURCE, PY_COMPILED, C_EXTENSION, PKG_DIRECTORY, C_BUILTIN, PY_FROZEN):
            return ret[3]

    else:
        if not os.path.exists(fpath):
            return

        #
        # the redundnacy of type-postfixes requires now prefix-analysis by '_scname'
        #
        
        # In [1]: from importlib.machinery import SOURCE_SUFFIXES, DEBUG_BYTECODE_SUFFIXES
        #    ...: , OPTIMIZED_BYTECODE_SUFFIXES, BYTECODE_SUFFIXES, EXTENSION_SUFFIXES
        # 
        # In [3]: SOURCE_SUFFIXES
        # Out[3]: ['.py']
        # 
        # In [4]: DEBUG_BYTECODE_SUFFIXES
        # Out[4]: ['.pyc']
        # 
        # In [5]: OPTIMIZED_BYTECODE_SUFFIXES
        # Out[5]: ['.pyc']
        # 
        # In [6]: BYTECODE_SUFFIXES
        # Out[6]: ['.pyc']
        # 
        # In [7]: EXTENSION_SUFFIXES
        # Out[7]: ['.cpython-36m-x86_64-linux-gnu.so', '.abi3.so', '.so']

        x = _scname.findall(fpath)
        if x:
            x = x[0]  # trust...
        else:
            x = os.path.splitext(fpath)

        if x[-1] in SOURCE_SUFFIXES:
            return __MT_SOURCE
        elif x[-1] in EXTENSION_SUFFIXES:
            return __MT_EXTENSION
        elif x[-1] in BYTECODE_SUFFIXES and not x[-2]:
            return __MT_COMPILED
        elif x[-1] in OPTIMIZED_BYTECODE_SUFFIXES and x[-2]:
            if x[-2] == 'opt-1':
                return __MT_COMPILED_OPT1
            if x[-2] == 'opt-2':
                return __MT_COMPILED_OPT2
            raise PySourceInfoError(
                "Unknown opt:" + str(x[-2]) + " " + str(fpath))
        elif x[-1] in DEBUG_BYTECODE_SUFFIXES:
            return __MT_COMPILED_DEBUG
    return __MT_UNKNOWN


def get_oid_filepathname(oid, spath=None):
    """File path name for OID."""
    find_spec = util.find_spec(oid, spath)
    if not find_spec is None:
        return find_spec.origin


def getpythonpath(pname, plist=None, **kw):
    """Matches prefix from sys.path."""
    if not plist:
        plist = sys.path
    _fp = os.path.normpath(os.path.abspath(pname))
    _presolve = kw.get('presolve', presolve)
    _buf = ''
    for _sp in plist:
        _sp = os.path.normpath(os.path.abspath(_sp))
        if _fp and _fp.startswith(_sp):
            if _presolve == P_FIRST:
                return _sp
            elif _presolve == P_LAST:
                _buf = _sp
            elif _presolve == P_LONGEST:
                if len(_sp) > len(_buf):
                    _buf = _sp
            elif _presolve == P_SHORTEST:
                if len(_sp) < len(_buf) or not _buf:
                    _buf = _sp
    return _buf


def getpythonpath_rel(fpname, plist=None, **kw):
    """Relative path name for first match on plist."""
    _p = getpythonpath(fpname, plist, **kw)
    if not _p:
        return
    ret = os.path.normpath(fpname)[len(_p):]
    if ret and ret[0] == os.path.sep:
        return ret[1:]
    return ret


def getstack_frame(spos=1, fromtop=False):
    """List of current mem-addresses on stack frames."""
    if fromtop:
        return stack()[-1 * spos]
    return stack()[spos]


def getstack_len():
    """Length of current stack."""
    return len(stack())

def matchpath(path, pathlist=None, pmatch=P_FIRST):
    """Match a file pathname of pathname on a pathlist."""
    _buf = None
    if pathlist == None:
        pathlist = sys.path
        
    if pmatch & P_IGNORE0:
        _pl = pathlist[1:]
    else:
        _pl = pathlist
    for sx in _pl:
        p0 = os.path.normpath(sx)
        if path.startswith(p0):
            if pmatch & P_FIRST:
                return p0
            elif pmatch & P_LAST:
                _buf = p0
            elif pmatch & P_LONGEST:
                if len(p0) > len(_buf):
                    _buf = p0
            elif pmatch & P_SHORTEST:
                if len(p0) < len(_buf) or not _buf:
                    _buf = p0
    return _buf

