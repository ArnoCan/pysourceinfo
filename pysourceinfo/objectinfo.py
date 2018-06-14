# -*- coding: utf-8 -*-
"""PySourceInfo - runtime type and source information on Python.

Based on the stack-frames of **inspect**, main parameter is **spos** 
- stack position. 

* *spos=1* is caller, *spos=2* is caller-of-caller, etc.. 

* 'r' is a regular expression for 'search()'.

Details see @local-manuals or @[https://pythonhosted.org/pysourceinfo/]
"""
from __future__ import absolute_import

import os
import sys
import re
from inspect import stack, getmodule, ismodule

from imp import is_builtin, is_frozen, find_module
from types import ModuleType, BuiltinFunctionType, BuiltinMethodType

from pysourceinfo import PySourceInfoError, V3K, \
    MT_UNKNOWN, MT_SOURCE, MT_COMPILED, MT_EXTENSION, MT_DIRECTORY, MT_BUILTIN, MT_FROZEN, \
    MT_COMPILED_OPT, MT_COMPILED_OPT1, MT_COMPILED_OPT2, MT_COMPILED_DEBUG

if V3K:
    from importlib import find_loader  # @UnresolvedImport


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2017 Arno-Can Uestuensoez" \
    " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.21'
__uuid__ = '9de52399-7752-4633-9fdc-66c87a9200b8'

__docformat__ = "restructuredtext en"


def getcaller_module(spos=1):
    """Caller module."""
    _sf = stack()
    if spos >= len(_sf):
        return None
    return getmodule(_sf[spos][0])


def getcaller_module_name(spos=1):
    """Name of caller module, else *None*."""
    _sf = stack()
    if len(_sf) <= spos:
        return None
    module = getmodule(_sf[spos][0])
    if module:  # seems to be more accurate than getmodule_name
        if module.__name__ == '__main__':
            return os.path.basename(os.path.splitext(_sf[spos][1])[0])
        return module.__name__


def getcaller_module_name_sub(spos=1):
    """Name from package to module."""

    # TODO:
    _sf = stack()
    if len(_sf) <= spos:
        return None
    module = getmodule(_sf[spos][0])
    if module:
        return module.__name__  # seems to be more accurate than getmodule_name


def getcaller_module_oid(spos=1):
    """OID of caller module."""
    return getmodule_oid(getcaller_module(spos + 1))


def getcaller_module_oid_sub(spos=1):
    """OID of caller module."""
    return getmodule_oid_sub(getcaller_module_oid(spos))


def getcaller_name(spos=1):
    """Name of caller."""
    return stack()[spos][3]


def getcaller_package_name(spos=1):
    """Name of first matching package containing the caller.
    The package is defined as the the first part
    of the module name.
    """
    _sf = stack()
    if len(_sf) < spos:
        return None
    module = getmodule(_sf[spos][0])
    if module and module.__package__:
        return re.sub("^([^.]+).*", r'\1', module.__package__)
    else:
        return re.sub("^([^.]+).*", r'\1', getcaller_module_name(spos + 1))


def getmodule_by_id(i):
    """Loaded module by ID."""
    if i:
        return [x for x in sys.modules.values() if id(x) == i][0]


def getmodule_by_name(n):
    """Loaded module by given name."""
    if n and sys.modules.get(n):
        return sys.modules[n]


_gmn = re.compile(r'^.*[.]')


def getmodule_name(mod):
    """Name similar to basename of loaded module, same as getmodule_oid."""
    if mod and ismodule(mod) and hasattr(mod, '__name__'):
            return _gmn.sub('', mod.__name__)


def getmodule_name_sub(mod):
    """Name relative to PYTHONPATH/sys.path of loaded module, same as getmodule_oid_sub."""
    if mod and ismodule(mod) and hasattr(mod, '__name__'):
        return re.sub(r'^[^.]*[.]', r'', mod.__name__)


def getmodule_oid(mod):
    """Name relative to PYTHONPATH/sys.path of loaded module."""
    if mod and ismodule(mod) and hasattr(mod, '__name__'):
        return mod.__name__


def getmodule_oid_sub(mod):
    """Name relative to PYTHONPATH/sys.path of loaded module."""
    if mod and ismodule(mod):
        if hasattr(mod, '__name__'):
            return re.sub(r'^[^.]*[.]', r'', mod.__name__)


def getmodule_package_name(mod):
    """Name of package for loaded module."""
    mn = getmodule_name(mod)
    if mn:
        if hasattr(mod, '__name__'):
            return mod.__name__


def getmodule_type(mod):
    """Type for loaded module as defined by module 'imp.*'"""
    if not V3K:
        try:
            ret = find_module(getmodule_oid(mod))
            if ret and ret[2]:
                if type(ret[2]) is int:  # MT_SOURCE,MT_COMPILED,MT_EXTENSION
                    return ret[2]
                elif type(ret[2]) is tuple:  # MT_DIRECTORY,MT_BUILTIN
                    return ret[2][2]
                # TODO: PY_FROZEN
        except:
            if ismodule(mod) or type(mod) is ModuleType:
                try:
                    _n = getmodule_oid(mod)
                    if _n in sys.builtin_module_names or is_builtin(_n):
                        return MT_BUILTIN
                    else:
                        bn = sys.modules[_n].__file__
                        if bn:
                            bn = os.path.basename(bn)
                            if bn.startswith('__init__'):
                                return MT_DIRECTORY
                            elif bn[-2:] == 'py':
                                return MT_SOURCE
                            elif bn[-3:] in ('pyc',):
                                return MT_COMPILED_DEBUG
                            elif bn[-3:] in ('pyo'):
                                return MT_COMPILED_OPT  # either O1 or O2

                            elif bn[-3:] in ('so',):
                                return MT_EXTENSION
                            elif is_frozen(_n):
                                return MT_FROZEN
                except ImportError:
                    pass
                except:
                    raise
            return MT_UNKNOWN
    else:
        # PEP 3147 -- PYC Repository Directories
        ret = find_loader(getmodule_oid(mod))

        if ret and hasattr(ret, 'path'):
            # check python native
            cdir = os.path.dirname(ret.path) + os.path.sep + '__pycache__'
            if os.path.exists(cdir):
                v = '{0}{1}'.format(*sys.version_info[:2])
                mname = re.sub(r"^.*[.]", '', ret.name) + '.' + sys.implementation.cache_tag  # @UndefinedVariable
                for xf in os.walk(cdir):
                    for xi in xf[2]:
                        if xi.startswith(mname):
                            #
                            # for now supports: Python3, Pypy3
                            #
                            if xi[-3:]== "pyc":
                                return MT_COMPILED_DEBUG
                            elif xi[-3:]== "pyo":
                                if xi[-9:-4]== "opt-1":
                                    return MT_COMPILED_OPT1
                                if xi[-9:-4]== "opt-2":
                                    return MT_COMPILED_OPT2
                            else:
                                raise PySourceInfoError("Extension unknown:" + str(xi))

            else:
                return MT_SOURCE

        elif type(ret) in (BuiltinFunctionType, BuiltinMethodType,):
            return MT_BUILTIN

        else:
            _n = None
            if ret:

                if not hasattr(ret, 'name'):
                    if type(ret) == type:
                        # return MT_FROZEN
                        return MT_BUILTIN
                    else:
                        return MT_UNKNOWN
                else:
                    _n = ret.name
            else:
                try:
                    _n = getmodule_oid(mod)
                except ImportError:
                    pass
                except:
                    raise

            if _n in sys.builtin_module_names or is_builtin(_n):
                return MT_BUILTIN
            else:
                bn = sys.modules[_n].__file__
                if bn:
                    bn = os.path.basename(bn)
                    if bn.startswith('__init__'):
                        return MT_DIRECTORY
                    elif bn[-2:] == 'py':
                        return MT_SOURCE
                    elif bn[-3:] in ('pyc', 'pyo'):
                        return MT_COMPILED
                    elif bn[-3:] in ('so',):
                        return MT_EXTENSION
                    elif is_frozen(_n):
                        return MT_FROZEN

            return MT_UNKNOWN
