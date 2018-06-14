# -*- coding: utf-8 -*-
"""pysourceinfo.infolists - lists.

Details see @local-manuals or @[https://pythonhosted.org/pysourceinfo/]
"""
from __future__ import absolute_import

import os
import sys
import re
from itertools import groupby

from pysourceinfo.helper import getpythonpath, getpythonpath_rel

# if V3K:
    # from importlib.machinery import SOURCE_SUFFIXES,DEBUG_BYTECODE_SUFFIXES,
    #    OPTIMIZED_BYTECODE_SUFFIXES,BYTECODE_SUFFIXES,
    #    EXTENSION_SUFFIXES #@UnresolvedImport
    # from importlib import util #@UnresolvedImport


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2017 Arno-Can Uestuensoez" \
    " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.21'
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

def getsysmodules_filepathname_list(r=None):
    """Returns the list of file pathnames of all loaded modules."""
    if not r:
        return sorted([x.__file__ for x in sys.modules.values()
                       if x and hasattr(x, '__file__')])
    return sorted([x.__file__ for x in sys.modules.values()
                   if x and hasattr(x, '__file__') and re.search(re.escape(r), x.__file__)])


def getsysmodules_id_list(r=None):
    """Returns the list of the IDs of the loaded modules."""
    if not r:
        return sorted([id(x) for x in sys.modules.values() if x])
    return sorted([id(x) for x in sys.modules.values()
                   if x and re.search(str(r), str(id(x)))])


def getsysmodules_list(r=None):
    """Returns the list of the loaded modules."""
    if not r:
        ml = sorted([x for x in sys.modules.keys()
                     if sys.modules[x]])
        return map(lambda x: sys.modules[x], ml)
    ml = sorted([x for x in sys.modules.keys()
                 if sys.modules[x] and re.search(r, x)])
    return map(lambda x: sys.modules[x], ml)


def getsysmodules_name_list(r=None):
    """Returns the list of the loaded modules."""
    if not r:
        return sorted([x for x in sys.modules.keys()
                       if sys.modules[x]])
    return sorted([x for x in sys.modules.keys()
                   if sys.modules[x] and re.search(re.escape(r), x)])


def getsysmodules_pathname_list(r=None):
    """Returns the list of path names of the loaded modules."""
    if not r:
        return list(__sortu([os.path.normpath(os.path.dirname(x.__file__))
                             for x in sys.modules.values() if x and
                             hasattr(x, '__file__')]))
    return list(__sortu([os.path.normpath(os.path.dirname(x.__file__))
                         for x in sys.modules.values()
                         if x and hasattr(x, '__file__') and
                         re.search(re.escape(r), x.__file__)]))


def getsysmodules_pathname_rel_list(r=None, plist=None):
    """Returns for the loaded modules the list of
    path names relative to PYTHONPATH.
    """
    if not r:
        return list(__sortu([getpythonpath_rel(x.__file__, plist)
                             for x in sys.modules.values()
                             if x and hasattr(x, '__file__')]))
    return list(__sortu([getpythonpath_rel(x.__file__, plist)
                         for x in sys.modules.values()
                         if x and hasattr(x, '__file__') and
                         re.search(re.escape(r), x.__file__)]))


def getsysmodules_python_pathname_list(r=None, plist=None):
    """Returns the list of path names for the loaded modules
    from PYTHONPATH."""
    if not r:
        return list(__sortu([getpythonpath(x.__file__, plist)
                             for x in sys.modules.values()
                             if x and hasattr(x, '__file__')]))
    return list(__sortu([getpythonpath(x.__file__, plist)
                         for x in sys.modules.values()
                         if x and hasattr(x, '__file__') and
                         re.search(re.escape(r), x.__file__)]))


