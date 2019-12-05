# -*- coding: utf-8 -*-
"""pysourceinfo.infolists - lists.

Details see @local-manuals or @[https://pythonhosted.org/pysourceinfo/]
"""
from __future__ import absolute_import

import os
import sys
import re
from itertools import groupby

from sourceinfo import P_LONGEST, P_SHORTEST
from sourceinfo.helper import getpythonpath, getpythonpath_rel


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2018 Arno-Can Uestuensoez" \
    " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.34'
__uuid__ = '9de52399-7752-4633-9fdc-66c87a9200b8'

__docformat__ = "restructuredtext en"


#---
#
# redundant for autonomous load-independence by reduction of dependencies
#


def __sortu(sequence):
    """sort unique"""
    return (x[0] for x in groupby(sorted(sequence)))


#---

def getsysmodules_filepathname_list(spat=None, **kargs):
    """Returns the list of file pathnames of all loaded modules
    from *sys.modules*.

    Args:
        spat:
            Search pattern, if provided it is used as pattern
            to search on each module name, returns matches only.
            Else returns the whole list.

        kargs:
            abs:
                If *True* transforms each module name by  
                *helper.getpythonpath* before further
                processing.

                default := False

    Returns:
        Returns the list of file path names for the loaded modules,
        or empty list.

    Raises:
        pass-through

    """
    _abs =  kargs.get('abs')

    if not spat:
        if _abs:
            return sorted(
                [
                    getpythonpath(x.__file__, ispre=True) + x.__file__ for x in sys.modules.values()
                    if x and hasattr(x, '__file__') and x.__file__ 
                ]
            )
        else:
            return sorted(
                [
                    x.__file__ for x in sys.modules.values()
                    if x and hasattr(x, '__file__') and x.__file__
                ]
            )

    if kargs.get('abs'):
        _res = []
        for x in sys.modules.values():
            if x and hasattr(x, '__file__') and x.__file__:
                if re.search(re.escape(spat), x.__file__):
                    _mp = getpythonpath(x.__file__, ispre=True, presolve=P_LONGEST)
                    _mprel = getpythonpath_rel(x.__file__, ispre=True, presolve=P_SHORTEST)
            
                if os.path.isabs(x.__file__):
                    if re.search(re.escape(spat), x.__file__):
                        _res.append(x.__file__)
                else:
                    _mp = getpythonpath(x.__file__, ispre=True, presolve=P_LONGEST)
                    _mprel = getpythonpath_rel(x.__file__, presolve=P_SHORTEST)

                    if _mp:
                        _sx = re.search(re.escape(spat), _mp + _mprel)
                        if _sx:
                            _res.append(_mp + _mprel)

        return sorted(_res)

    else:
        return sorted(
            [
                x.__file__ for x in sys.modules.values()
                if x and hasattr(x, '__file__') and x.__file__ and re.search(re.escape(spat), x.__file__)
            ]
        )

def getsysmodules_id_list(r=None):
    """Returns the list of the IDs of the loaded modules.

    Args:
    
        r: 
            regexpr to be applied on the IDs.
    
    Returns:
    
        Returns the list of the loaded modules.
    
    Raises:
    
        pass-through

    """
    if not r:
        return sorted([id(x) for x in sys.modules.values() if x])
    return sorted([id(x) for x in sys.modules.values()
                   if x and re.search(str(r), str(id(x)))])


def getsysmodules_list(r=None):
    """Returns the list of the loaded modules.
    
    Args:
        r:
            regexpr to be applied on the module names.
    
    Returns:
        Returns the list of the loaded modules.
    
    Raises:
        pass-through

    """
    if not r:
        ml = sorted([x for x in sys.modules.keys()
                     if sys.modules[x]])
        return map(lambda x: sys.modules[x], ml)
        
    ml = sorted([x for x in sys.modules.keys()
                 if sys.modules[x] and re.search(r, x)])
    return map(lambda x: sys.modules[x], ml)


def getsysmodules_name_list(r=None):
    """Returns the list of the loaded modules.

    Args:
        r:
            regexpr to be applied on the module names.
    
    Returns:
        Returns the list of the names of the loaded modules.
    
    Raises:
        passed through exceptions

    """
    if not r:
        return sorted([x for x in sys.modules.keys()
                       if sys.modules[x]])
    return sorted([x for x in sys.modules.keys()
                   if sys.modules[x] and re.search(re.escape(r), x)])


def getsysmodules_pathname_list(r=None):
    """Returns the list of path names of the loaded modules.
    
    Args:
        r:
            regexpr to be applied on the module path names.
    
    Returns:
        Returns the list of pathnames of the loaded modules.
    
    Raises:
        pass-through

    """
    if not r:
        return list(__sortu([os.path.normpath(os.path.dirname(x.__file__))
                             for x in sys.modules.values() if x and hasattr(x, '__file__') and x.__file__]))
    return list(__sortu([os.path.normpath(os.path.dirname(x.__file__))
                         for x in sys.modules.values()
                         if x and hasattr(x, '__file__') and x.__file__ and re.search(re.escape(r), x.__file__)]))


def getsysmodules_pathname_rel_list(r=None, plist=None):
    """Returns for the loaded modules the list of
    path names relative to PYTHONPATH.

    Args:
        r:
            regexpr to be applied on the module path names.
        
        plist:
            alternate search path list
    
    Returns:
        Returns the list of pathnames of the loaded modules.
    
    Raises:
        pass-through
    
    """
    if not r:
        return list(__sortu([getpythonpath_rel(x.__file__, plist)
                             for x in sys.modules.values()
                             if x and hasattr(x, '__file__') and x.__file__]))
    return list(__sortu([getpythonpath_rel(x.__file__, plist)
                         for x in sys.modules.values()
                         if x and hasattr(x, '__file__') and x.__file__ and re.search(re.escape(r), x.__file__)]))


def getsysmodules_python_pathname_list(pname=None, plist=None, **kargs):
    """Returns the list of packages path names for the loaded
    modules from PYTHONPATH. This is as mentioned related to the
    containing package itself.

    Args:
        
        **pname**:
            pathname

        **plist**:
            Search path list.
            
            default := sys.path

        kargs:
            **presolve**:
                The type of path resolution: ::

                   presolve := (
                        P_FIRST
                      | P_LAST
                      | P_LONGEST
                      | P_SHORTEST
                   )

                default := pysourceinfo.presolve(P_FIRST)

    Returns:
        List of paths

    Raises:
        pass-through

    """
    if not pname:
        return list(__sortu([getpythonpath(x.__file__, plist, **kargs)
                             for x in sys.modules.values()
                             if x and hasattr(x, '__file__') and x.__file__]))
    return list(__sortu([getpythonpath(x.__file__, plist, **kargs)
                         for x in sys.modules.values()
                         if x and hasattr(x, '__file__') and x.__file__ and re.search(re.escape(pname), x.__file__)]))


