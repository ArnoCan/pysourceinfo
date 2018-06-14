# -*- coding: utf-8 -*-
"""pysourceinfo.fileinfo - information on source files.

Based on the stack-frames of *inspect*, *__file__*, and additional 
attributes.

Details see @local-manuals or @[https://pythonhosted.org/pysourceinfo/]
"""
from __future__ import absolute_import
from __future__ import print_function

import os
import sys
import re

from inspect import stack, getmodule, isbuiltin, ismodule, getsourcefile

from pysourceinfo import V3K
from pysourceinfo import presolve
from pysourceinfo.helper import matchpath, getpythonpath, getpythonpath_rel

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2017 Arno-Can Uestuensoez" \
    " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.21'
__uuid__ = '9de52399-7752-4633-9fdc-66c87a9200b8'

__docformat__ = "restructuredtext en"


if V3K:
    vers = '{0}{1}'.format(*sys.version_info[:2])   # pylint: disable-msg=W0142


#---
#
# redundant for autonomous load-independence by reduction of dependencies
#
__gmn = re.compile(r'^.*[.]')
def __getmodule_name(mod):
    #"""Name similar to basename of loaded module, same as getmodule_oid."""
    if mod and ismodule(mod):
        if hasattr(mod, '__name__'):
            return __gmn.sub('', mod.__name__)
#---

def getcaller_filename(spos=1):
    """Filename of caller's module."""
    return os.path.basename(getcaller_filepathname(spos))


def getcaller_filepathname(spos=1):
    """File pathname of caller's module."""
    _sf = stack()
    return os.path.abspath(_sf[spos][1])


def getcaller_filepathname_rel(spos=1):
    """File pathname of caller's module relative to sys.path."""
    _sf = stack()
    _cf = os.path.abspath(os.path.normpath(_sf[spos][1]))
    for sx in sys.path:
        if _cf.startswith(sx):
            return _cf[len(os.path.normpath(sx))]


def getcaller_linenumber(spos=1):
    """Source line number of call."""
    return stack()[spos][2]


def getcaller_linenumber_def(spos=1):
    """First line number of enclosing caller function/method definition."""
    return stack()[spos][0].f_code.co_firstlineno

def getcaller_package_filename(spos=1):
    return os.path.basename(getcaller_package_filepathname(spos))


__comp_package_filepathname = re.compile(r"""
    (
        ([/\\\\]*([^/\\\\]+.py)[oc]{0,1}$)
        | ([/\\\\]*([^/\\\\]+).*.py[oc]{0,1}$)
        | ([/\\\\]*([^/\\\\]+).*$)
    )
    """, re.VERBOSE
)
def getcaller_package_filepathname(spos=1, pmatch=presolve):
    """Filepathname of the package from *sys.path*."""
    _sf = stack()
    _cf = os.path.normpath(os.path.abspath(_sf[spos][1]))

    p0 = matchpath(_cf, sys.path, pmatch)

    p0l = len(p0)
    p1 = getcaller_filepathname(spos + 1)[p0l:]
    pfn = __comp_package_filepathname.search(p1)

    # TODO: PEP420 - Implicit Namespace Packages

    if pfn.start(2) != -1:
        return p0 + os.path.sep + pfn.group(3)
    elif pfn.start(4) != -1:
        return p0 + os.path.sep + pfn.group(5)
    elif pfn.start(6) != -1:
        return p0 + os.path.sep + pfn.group(7)
    return None


def getcaller_package_pathname(spos=1, pmatch=presolve):
    """Pathname of the package from *sys.path* as used for search of the package."""
    return os.path.dirname(getcaller_package_filepathname(spos+1, pmatch))


def getcaller_pathname(spos=1):
    """pathname of caller source file."""
    if not V3K:
        return os.path.dirname(getcaller_filepathname(spos + 1))
    else:
        _sf = stack()
        # mx = _sf[spos][0].f_locals['module']
        module = getmodule(_sf[spos][0])
        if hasattr(module, '__file__'):
            f = module.__file__
            return os.path.dirname(f)
        # PEP 3147 -- PYC Repository Directories


__comp_getcaller_pathname_rel = re.compile(r"""
    (
     (()[/\\\\]*[^/\\\\]+.py[oc]{0,1}$)
     |([/\\\\]*(.+)[/\\\\][^/\\\\]+.py[oc]{0,1}$)
     |([/\\\\]*(.+))
    )
    """, re.VERBOSE
)


def getcaller_pathname_rel(spos=1):
    """Relative pathname to first matching package directory of caller."""
    ax = os.path.normpath(getcaller_filepathname(
        spos + 1))  # TODO: check for normpath
    for si in sys.path:
        si = os.path.normpath(si) 
        if ax.startswith(si):
            gx = __comp_getcaller_pathname_rel.search(ax[len(si):])
            if gx.start(3) != -1:
                return gx.group(3)
            elif gx.start(5) != -1:
                return gx.group(5)
            elif gx.start(7) != -1:
                return gx.group(7)
            return None


def getcaller_pathname_sub(spos=1):
    """sub-pathname to first matching module directory of caller."""
    return re.sub(r"[^/\\\\]*[/\\\\](.*)", r"\1", getcaller_pathname_rel(spos + 1))


def getcaller_python_pathname(spos=1):
    """Alias for getcaller_package_pathname."""
    return getcaller_package_pathname(spos + 1)


def getcaller_source_filepathname(spos=1):
    """Pathname of caller source."""
    return os.path.abspath(getsourcefile(stack()[spos][0]))  # mx = _sf[spos][1]


def getmodule_filename(mod):
    """Basename of file for loaded module *mod*."""
    if mod and ismodule(mod) and not isbuiltin(mod):
        if hasattr(mod, '__file__') and os.path.exists(mod.__file__):
            return os.path.basename(mod.__file__)


def getmodule_filepathname(mod):
    """File pathname of loaded module *mod*."""
    if mod and ismodule(mod) and not isbuiltin(mod):
        return os.path.abspath(getsourcefile(mod))


def getmodule_package_pathname(mod):
    """Path name of package for loaded module."""
    mn = __getmodule_name(mod)  # requires normalized path
    if mn:
        mpn = getmodule_pathname(mod)
        return mpn[:len(mpn) + 1]


def getmodule_pathname(mod):
    """Path name of loaded module."""
    if mod and ismodule(mod) and not isbuiltin(mod):
        if hasattr(mod, '__file__'):
            return os.path.normpath(os.path.dirname(mod.__file__))


def getmodule_pathname_rel(mod, plist=None):
    """Relative path name to PYTHONPATH for loaded module."""
    if mod and ismodule(mod) and not isbuiltin(mod):
        if hasattr(mod, '__file__'):
            return getpythonpath_rel(mod.__file__, plist)


def getmodule_pathname_sub(mod, plist=None):
    """Path name for loaded module, relative to package path ."""
    ax = getmodule_pathname_rel(mod, plist)
    if not V3K:
        return re.sub(r"[^/\\\\]*[/\\\\]", r"\1", ax)
    else:
        return re.sub(r"[^/\\\\]*[/\\\\]".encode('utf-8'), r"\1".encode('utf-8'), ax)


def getmodule_python_pathname(mod, plist=None):
    """Path name from PYTHONPATH of loaded module."""
    if mod and ismodule(mod) and not isbuiltin(mod):
        if hasattr(mod, '__file__'):
            return getpythonpath(mod.__file__, plist)

