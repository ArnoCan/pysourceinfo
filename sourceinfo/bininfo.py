# -*- coding: utf-8 -*-
"""pysourceinfo.bininfo - runtime information on compiled Python binaries.

Details see manuals.
"""
from __future__ import absolute_import
from __future__ import print_function

import os
import sys
import re
from inspect import stack, getmodule, isbuiltin, ismodule

from pythonids import PYV3


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2017 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.34'
__uuid__ = '9de52399-7752-4633-9fdc-66c87a9200b8'

__docformat__ = "restructuredtext en"

#---
#
# redundant for autonomous load-independence by reduction of dependencies
#
def __getpythonpath_rel(fpname, plist=None):
    """Relative path name for first match on plist."""
    if not plist:
        plist = sys.path
    # for now dirs with terminating os.sep
    _fp = os.path.normpath(os.path.abspath(fpname))
    _fp = re.escape(_fp)
    for _sp in plist:
        _sp = os.path.normpath(os.path.abspath(_sp))
        _sp = re.escape(_sp)
        if _fp and _fp.startswith(_sp):
            _r = _fp.replace(_sp, "")
            if _r and _r[0:2] == re.escape(os.sep):
                return re.sub(r'\\(.)', r'\1', _r[2:])
            elif _r and _r[0] == os.sep:
                return re.sub(r'\\(.)', r'\1', _r[1:])
            if not _r:
                return '.'
            return re.sub(r'\\(.)', r'\1', _r)
#---


def getcaller_bin_filename(spos=1):
    """Filename of binary caller module.

    Args:
        spos:
            Caller position on the stack.
    
    Returns:
        Returns the filename.
    
    Raises:
        pass-through

    """
    return os.path.basename(getcaller_bin_filepathname(spos))


def getcaller_bin_filepathname(spos=1):
    """File pathname of caller module.
    
    Args:
        spos:
            Caller position on the stack.
    
    Returns:
        Returns the file pathname.
    
    Raises:
        pass-through

    """
    _sf = stack()
    if spos >= len(_sf):
        return None
    module = getmodule(_sf[spos][0])
    if not PYV3:
        if module:
            return os.path.abspath(module.__file__)  # source
    else:
        # PEP 3147 -- PYC Repository Directories
        ret = find_loader(module.__name__)  #@UndefinedVariable
        if ret and hasattr(ret, 'path'):
            # check python native
            cdir = os.path.dirname(ret.path) + os.path.sep + '__pycache__'
            if os.path.exists(cdir):
                mname = re.sub(r"^.*[.]", '', ret.name)
                for xf in os.walk(cdir):
                    res = None
                    for xi in xf[2]:
                        if vers == re.sub(  #@UndefinedVariable
                                         mname + r".cpython-(3[0-9]).py[co]$", r'\1', xi):
                            res = cdir + os.path.sep + xi
                            if res[-1] == 'o':  # prio over '.pyc' on '.pyo'
                                break
                    return res
            else:
                return ret.path
        else:
            if ret:
                if hasattr(ret, 'name'):
                    fn = ret.get_filename(module.__name__)
                    # fd = ret.get_data(fn)
                    return fn

            # FIXME: module.__name__ => 'baseOID'
            if module.__name__ in sys.builtin_module_names:
                return None
            else:
                bn = sys.modules[module.__name__].__file__
                if bn and os.path.exists(bn):
                    return bn

def getcaller_bin_pathname(spos=1):
    """pathname of caller source file.
    
    Args:
        spos:
            Caller position on the stack.
    
    Returns:
        Returns the filename.
    
    Raises:
        passed through exceptions

    """
    if not PYV3:
        return os.path.dirname(getcaller_bin_filepathname(spos + 1))
    else:
        _sf = stack()
        module = getmodule(_sf[spos][0])
        if hasattr(module, '__file__'):
            f = module.__file__
            return os.path.dirname(f)
        # PEP 3147 -- PYC Repository Directories


def getcaller_bin_pathname_rel(spos=1):
    """Relative pathname to first matching package directory of caller.
    Evaluates 'sys.path' first, else switches to 'inspect'.
    
    Args:
        spos:
            Caller position on the stack.
    
    Returns:
        Returns the path name to the package.
    
    Raises:
        pass-through

    """
    ax = os.path.normpath(getcaller_bin_filepathname(
        spos + 1))  # TODO: check for normpath
    for si in sys.path:
        si = os.path.normpath(si)
        if ax.startswith(si):
            return re.sub(si + r"[/\\\\]*(.+?)[/\\\\]*[^/\\\\]+.py[oc]*$", r"\1", ax)


def getcaller_bin_pathname_sub(spos=1):
    """sub-pathname to first matching module directory of caller.
    Evaluates 'sys.path' first, else switches to 'inspect'.
    
    Args:
        spos:
            Caller position on the stack.
    
    Returns:
        Returns the path name to the package.
    
    Raises:
        passed through exceptions

    """
    ax = getcaller_bin_pathname_rel(spos + 1)
    return re.sub(r"[^/\\\\]*[/\\\\](.*)", r"\1", ax)


def getmodule_bin_filename(mod):
    """Basename of file for loaded module *mod*.
    
    Args:
        mod:
            Reference to a loaded module.
    
    Returns:
        Returns the basename of the loaded module.
    
    Raises:
        passed through exceptions

    """
    if mod and ismodule(mod) and not isbuiltin(mod):
        if hasattr(mod, '__file__') and os.path.exists(mod.__file__):
            return os.path.basename(mod.__file__)


def getmodule_bin_filepathname(mod):
    """File pathname of loaded module *mod*.

    Args:
        mod:
            Reference to a loaded module.
    
    Returns:
        Returns the file pathname of the loaded module.
    
    Raises:
        pass-through

    """
    if mod and ismodule(mod) and not isbuiltin(mod):
        if hasattr(mod, '__file__') and os.path.exists(mod.__file__):
            return os.path.abspath(os.path.normpath(mod.__file__))


def getmodule_bin_pathname(mod):
    """Path name of loaded module.
    
    Args:
        mod:
            Reference to a loaded module.
    
    Returns:
        Returns the pathname of the loaded module.
    
    Raises:
        pass-through

    """
    if mod and ismodule(mod) and not isbuiltin(mod):
        if hasattr(mod, '__file__'):
            return os.path.normpath(os.path.dirname(mod.__file__))


def getmodule_bin_pathname_rel(mod, plist=None):
    """Relative path name to PYTHONPATH for loaded module.

    Args:
        mod:
            Reference to a loaded module.
    
    Returns:
        Returns the relative pathname of the loaded module.
    
    Raises:
        pass-through
    
    """
    if mod and ismodule(mod) and not isbuiltin(mod):
        if hasattr(mod, '__file__'):
            return __getpythonpath_rel(mod.__file__, plist)


def getmodule_bin_pathname_sub(mod, plist=None):
    """Path name for loaded module, relative to package path.
    
    Args:
        mod:
            Reference to a loaded module.
    
    Returns:
        Returns the sub pathname of the loaded module.
    
    Raises:
        passed through exceptions

    """
    ax = getmodule_bin_pathname_rel(mod, plist)
    if not PYV3:
        return re.sub(r"[^/\\\\]*[/\\\\]", r"\1", ax)
    else:
        return re.sub(r"[^/\\\\]*[/\\\\]".encode('utf-8'), r"\1".encode('utf-8'), ax)
