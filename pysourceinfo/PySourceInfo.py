# -*- coding: utf-8 -*-
"""PySourceInfo - runtime type information on Python source location: package, module, and caller.

This modules provides for the location of Python execution
by means of the package 'inspect' extended by additional sources
for a simple API.

The stack frame of inspect is in particular reduced to the common
parameter 'spos', which is an abstraction of the 'stack-position'
representing the level of history within the caller level.
The value 'spos==0' is the function itself, whereas 'spos==1' is the
first level caller. Consequently 'spos==2' is the caller of the caller,
etc.

The categories of provided RTTI comprise:

* **packages** - Python packages.

* **modules** - Python modules - a.k.a. source files.

* **callers** - Python functions and class/object methods.


Where the following attributes are available:

* name(package, module, function)

* OID - dotted relative path to matching item of sys.path

* filename

* filepathname

* item of sys.path

* relative path to item of sys.path

* line number

Dependent on the call context, some of the attribute values may
not be available.
E.g. when called from within the python/ipython shell, or 'main'.

The API is designed here as a collection of slim functions
only in order to avoid any overhead for generic application.

"""
from __future__ import absolute_import
from inspect import ismethod
#from mpl_toolkits.axes_grid1.axes_size import Padded
#from scipy.stats.distributions import instancemethod

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.7'
__uuid__='9de52399-7752-4633-9fdc-66c87a9200b8'

__docformat__ = "restructuredtext en"

import os,sys
version = '{0}.{1}'.format(*sys.version_info[:2])
if version < '2.7': # pragma: no cover
    raise Exception("Requires Python-2.7.* or higher")

import inspect,re


class PySourceInfoException(Exception):
    pass

def getCallerFileName(spos=1):
    """Returns the filename of caller source file.

    Args:
        spos: Caller position on the stack.

    Returns:
        Returns the filename.

    Raises:
        passed through exceptions:
    """
    return os.path.basename(getCallerFilePathName(spos))

def getCallerFilePathName(spos=1):
    """Returns the pathname of caller source file.

    Args:
        spos: Caller position on the stack.

    Returns:
        Returns the filepathname.

    Raises:
        passed through exceptions:
    """
    return os.path.abspath(inspect.stack()[spos][1])

def getCallerFunc(spos=1):
    """Returns the ID:=mem-address of caller function.

    Args:
        spos: Caller position on the stack.

    Returns:
        Returns the ID:=mem-address.

    Raises:
        passed through exceptions:
    """
    return inspect.stack()[spos][0]

def getCallerFuncName(spos=1):
    """Returns the name of caller function.

    Args:
        spos: Caller position on the stack.

    Returns:
        Returns the filepathname.

    Raises:
        passed through exceptions:
    """
    return inspect.stack()[spos][3]

def getCallerLinenumber(spos=1):
    """Returns the line number of caller.

    Args:
        spos: Caller position on the stack.

    Returns:
        Returns the filepathname.

    Raises:
        passed through exceptions:
    """
    return inspect.stack()[spos][2]

def getCallerModule(spos=1):
    """Returns the caller module.

    Args:
        spos: Caller position on the stack.

    Returns:
        Returns the caller module.

    Raises:
        passed through exceptions:
    """
    _sf = inspect.stack()
    if len(_sf) < spos:
        return None
    return inspect.getmodule(_sf[spos][0])

def getCallerModuleFilePathName(spos=1):
    """Returns the filepathname of the module.

    Args:
        spos: Caller position on the stack.

    Returns:
        Returns the filepathname of the caller module.

    Raises:
        passed through exceptions:
    """
    _sf = inspect.stack()
    if len(_sf) < spos:
        return None
    module = inspect.getmodule(_sf[spos][0])
    if module:
        if module.__file__[-4:-1] == '.py': 
            return os.path.abspath(module.__file__[:-1])
        return os.path.abspath(module.__file__)

def getCallerModuleName(spos=1):
    """Returns the name of the caller module.

    Both approaches for evaluation the actual relative
    module name seem to have their own challenges,
    module.__name__ and inspect.getmodulename.

    Args:
        spos: Caller position on the stack.

    Returns:
        Returns the name of caller module.
        The dotted object path is relative to
        the actual used sys.path item.

    Raises:
        passed through exceptions:
    """
    _sf = inspect.stack()
    if len(_sf) < spos:
        return None
    module = inspect.getmodule(_sf[spos][0])
    if module:
        return module.__name__ # seems to be more accurate than inspect.getmodulename

def getCallerModulePathName(spos=1):
    """Returns the pathname of the module.

    Args:
        spos: Caller position on the stack.

    Returns:
        Returns the filepathname of module.

    Raises:
        passed through exceptions:
    """
    return os.path.dirname(getCallerModuleFilePathName(spos+1))

def getCallerModulePythonPath(spos=1):
    """Returns the prefix item from sys.path used for the caller module based on 'inspect'.

    Args:
        spos: Caller position on the stack.

    Returns:
        Returns the name of caller module.

    Raises:
        passed through exceptions:
    """
    _m = re.sub(ur".[^.]+$","",getCallerModuleName(spos+1) )
    if _m:
        return re.sub(ur"""[/\\\\]*"""+_m+"""[/\\\\]*$""","",getCallerModulePathName(spos+1))                     
    return getCallerModulePathName(spos+1)

def getCallerName(spos=1):
    """Returns the name of the caller.

    Args:
        spos: Caller position on the stack.

    Returns:
        Returns the filepathname.

    Raises:
        passed through exceptions:
    """
    return inspect.stack()[spos][3]

def getCallerNamespaceGlobal(spos=1):
    """Returns the global namespace of the caller.

    Args:
        spos: Caller position on the stack.

    Returns:
        Returns a reference to the callers global namespace.

    Raises:
        passed through exceptions:
    """
    return inspect.stack()[spos][0].f_globals

def getCallerNamespaceLocal(spos=1):
    """Returns the local namespace of the caller.

    Args:
        spos: Caller position on the stack.

    Returns:
        Returns a reference to the callers local namespace.

    Raises:
        passed through exceptions:
    """
    return inspect.stack()[spos][0].f_locals

def getCallerNameOID(spos=1):
    """Returns the name of the caller in dotted notation.

    Args:
        spos: Caller position on the stack.

    Returns:
        Returns the package name.

    Raises:
        passed through exceptions:
    """
    _spos = spos
    _sf = inspect.stack()
    if len(_sf) < _spos:
        return None
    _pf = _sf[_spos][0]
    _coid = inspect.getmodule(_pf)
    if _coid:
        _coid = _coid.__name__
    if 'self' in _pf.f_locals:
        _coid += "." + str(_pf.f_locals['self'].__class__.__name__)
    if _pf.f_code.co_name != '<module>':
        _coid += "." + str(_pf.f_code.co_name)
    del _pf
    return _coid

def getCallerPackageFilePathName(spos=1):
    """Returns the filepathname of the package containing the caller.

    Args:
        spos: Caller position on the stack.

    Returns:
        Returns the package name.

    Raises:
        passed through exceptions:
    """
    m0 = getCallerModuleName(spos+1)
    p0 = getCallerModuleFilePathName(spos+1)
    if m0.find('.') == -1:
        if p0[-4:] == '.pyc':
            return p0[:-1]
    pp0 = re.sub(m0+".py[co]*$","",ur""+p0)
    pp0 += re.sub(r'^([^.]+).*',r'\1',m0) + os.sep + '__init__.py'
    if os.path.exists(pp0):
        return pp0
    return p0

def getCallerPackageName(spos=1):
    """Returns the name of the first matching package containing the caller.

    Relies on 'inspect'.
    
    Args:
        spos: Caller position on the stack.

    Returns:
        Returns the package name when defined, else None.

    Raises:
        passed through exceptions:
    """
    _sf = inspect.stack()
    if len(_sf) < spos:
        return None
    module = inspect.getmodule(_sf[spos][0])
    if module and module.__package__:
        return module.__package__
    else:
        return re.sub("^([^.]+).*",r'\1',getCallerModuleName(spos+1))

def getCallerPackagePathName(spos=1):
    """Returns the pathname to the first matching package directory of the caller.

    Relies on 'inspect'.

    Args:
        spos: Caller position on the stack.

    Returns:
        Returns the path name to the package.

    Raises:
        passed through exceptions:
    """
    _sf = inspect.stack()
    if len(_sf) < spos:
        return None
    module = inspect.getmodule(_sf[spos][0])
    if module and module.__package__:
        return os.path.dirname(module.__file__)
    return re.sub(ur""+getCallerModuleName(spos+1)+'.py[co]*$','',getCallerModuleFilePathName(spos+1))

def getCallerPackagePythonPath(spos=1):
    """Returns the python path for first matching package of the caller.

    Relies on 'inspect'.

    Intentionally the same as 'getCallerPackagePathName'.

    Args:
        spos: Caller position on the stack.

    Returns:
        Returns the path name to the package.

    Raises:
        passed through exceptions:
    """
    return os.path.dirname(getCallerPackagePathName(spos+1))

def getCallerSysPathPackageName(spos=1):
    """Returns the name of the first matching package on sys.path.

    Evaluates 'sys.path' first, else switches to 'inspect'.
    
    Args:
        spos: Caller position on the stack.

    Returns:
        Returns the package name when defined, else None.

    Raises:
        passed through exceptions:
    """
    ax = os.path.normpath(getCallerModuleFilePathName(spos+1)) #TODO: check for normpath
    for si in sys.path:
        si = os.path.normpath(re.escape(si))
        if ax.startswith(si):
            return re.sub(ur""+si+ur"[/\\]*([^/\\]+)(((!(.py[oc]*))|([/\\])([/\\]*).*$)|(.py[oc]*)$)",ur"\1",ax)

    _sf = inspect.stack()
    if len(_sf) < spos:
        return None
    module = inspect.getmodule(_sf[spos][0])
    if module and module.__package__:
        return module.__package__
    else:
        return re.sub("^([^.]+).*",r'\1',getCallerModuleName(spos+1))

def getCallerSysPathPackageSysPathName(spos=1):
    """Returns the pathname to the first matching package directory of the caller.

    Evaluates 'sys.path' first, else switches to 'inspect'.

    Args:
        spos: Caller position on the stack.

    Returns:
        Returns the path name to the package.

    Raises:
        passed through exceptions:
    """
    ax = os.path.abspath(os.path.normpath(getCallerModuleFilePathName(spos+1))) #TODO: check for normpath
    for si in sys.path:
        si = os.path.normpath(si)
        if ax.startswith(si):
            return si

    _sf = inspect.stack()
    if len(_sf) < spos:
        return None
    module = inspect.getmodule(_sf[spos][0])
    if module and module.__package__:
        return os.path.dirname(module.__file__)
    return re.sub(ur""+getCallerModuleName(spos+1)+'.py[co]*$','',getCallerModuleFilePathName(spos+1))

def getCallerSysPathPackagePathNameRel(spos=1):
    """Returns the pathname to the first matching package directory of the caller.

    Evaluates 'sys.path' first, else switches to 'inspect'.

    Args:
        spos: Caller position on the stack.

    Returns:
        Returns the path name to the package.

    Raises:
        passed through exceptions:
    """
    ax = os.path.normpath(getCallerModuleFilePathName(spos+1)) #TODO: check for normpath
    for si in sys.path:
        si = os.path.normpath(si)
        if ax.startswith(si):
            return re.sub(ur""+si+ur"[/\\]*([^/\\]+)[/\\]*[^/\\]+.py[oc]*$",ur"\1",ax)
            break

    #FIXME: TODO!!!
#     _sf = inspect.stack()
#     if len(_sf) < spos:
#         return None
#     module = inspect.getmodule(_sf[spos][0])
#     if module and module.__package__:
#         return module.__package__
#     else:
#         return re.sub("^([^.]+).*",r'\1',getCallerModuleName(spos+1))

def getCallerSysPathPackagePythonPath(spos=1):
    """Returns the python path for first matching package of the caller.

    Evaluates 'sys.path' first, else switches to 'inspect'.

    Intentionally the same as 'getCallerPackagePathName'.

    Args:
        spos: Caller position on the stack.

    Returns:
        Returns the path name to the package.

    Raises:
        passed through exceptions:
    """
    return os.path.dirname(getCallerPackagePathName(spos+1))

def getCallerPathName(spos=1):
    """Returns the pathname of caller source file.

    Args:
        spos: Caller position on the stack.

    Returns:
        Returns the filename.

    Raises:
        passed through exceptions:
    """
    return os.path.dirname(getCallerFilePathName(spos+1))

def getModuleFilePathName(mod):
    """Returns the filepathname of the loaded module.

    Args:
        mod: Reference to a loaded module.

    Returns:
        Returns the filepathname of the loaded module.

    Raises:
        passed through exceptions:
    """
    if mod and inspect.ismodule(mod) and not inspect.isbuiltin(mod) :
        if os.path.exists(mod.__file__):
            return os.path.abspath(os.path.normpath(mod.__file__))

def getModulePathName(mod):
    """Returns the pathname of the loaded module.

    Args:
        mod: Reference to a loaded module.

    Returns:
        Returns the pathname of the loaded module.

    Raises:
        passed through exceptions:
    """
    if mod and inspect.ismodule(mod) and not inspect.isbuiltin(mod) :
        return os.path.abspath(os.path.normpath(os.path.dirname(mod.__file__)))

def getModuleSourceFilePathName(mod):
    """Returns the filepathname of the source code for loaded module.

    Args:
        mod: Reference to a loaded module.

    Returns:
        Returns the filepathname of the source for the loaded module,
        else None.

    Raises:
        passed through exceptions:
    """
    if mod and inspect.ismodule(mod) and not inspect.isbuiltin(mod) :
        f = os.path.splitext(mod.__file__)[0]+'.py'
        if os.path.exists(f):        
            return os.path.abspath(os.path.normpath(f)) 

def getPythonPathFromSysPath(pname,plist=None):
    """Gets the first matching prefix from sys.path.

    Foreseen to be used for canonical base reference in unit tests.
    This enables in particular for generic tests of filesystem positions
    where originally absolute pathnames were required.

    Args:
        pname: Pathname.

        plist: List of possible python paths.
            default := sys.path

    Returns:
        Returns the first matching path prefix from sys.path.

    Raises:
        passed through exceptions:
    """
    if not plist:
        plist = sys.path
    _fp = os.path.normpath(os.path.abspath(pname))
    for _sp in plist:
        _sp = os.path.normpath(os.path.abspath(_sp))
        if _fp and _fp.startswith(_sp):
            return _sp

def getPythonPathRel(fpname,plist=None):
    """Returns the relative path name for the first match on plist.

    REMARK: Refer also to 'getCallerNameSpceGlobal'.

    Args:
        fpname: The filepathname.

        plist: List of possible python paths.
            default := sys.path

    Returns:
        Returns the path postfix for fpname when found,
        else 'None'.

    Raises:
        passed through exceptions:
    """
    if not plist:
        plist = sys.path
        
    #FIXME:
    _fp = os.path.normpath(os.path.abspath(fpname)) # for now dirs with terminating os.sep
    _fp = re.escape(_fp)
    for _sp in plist:

        #FIXME:
        _sp = os.path.normpath(os.path.abspath(_sp))
        _sp = re.escape(_sp)
        if _fp and _fp.startswith(_sp):
            _r = _fp.replace(_sp,"")
            if _r and _r[0:2] == re.escape(os.sep):
                return re.sub(r'\\(.)', r'\1', _r[2:])
            elif _r and _r[0] == os.sep:
                return re.sub(r'\\(.)', r'\1', _r[1:])
            if not _r:
                return '.'
            return re.sub(r'\\(.)', r'\1', _r)

def getStackFuncNameList(fromtop=False):
    """Returns a list of current functions names on stack.

    Args:
        fromtop: If True, return the reversed list.
            
            default:=False

    Returns:
        Returns the list of function names on stack.

            fromtop==False:   stack[0] == result[0],...

            fromtop==True:    stack[0] == result[-1],... - reversed 

    Raises:
        passed through exceptions:

    """
    if fromtop:
        return map(lambda x:x[3], reversed(inspect.stack()))
    else:
        return map(lambda x:x[3], inspect.stack())

def getStackFuncList(fromtop=False):
    """Returns a list of current mem-addresses on the stack.

    Args:
        fromtop: If True, return the reversed list.
            
            default:=False

    Returns:
        Returns the list of function names on stack.

            fromtop==False:   stack[0] == result[0],...

            fromtop==True:    stack[0] == result[-1],... - reversed 

    Raises:
        passed through exceptions:

    """    
    if fromtop:
        return [ x[0] for x in reversed(inspect.stack())]
    return [ x[0] for x in inspect.stack()]

def getStackFuncMap(funp):
    """Returns a list of mem-addresses for each call of funcp on the stack.

    Args:
        funp: Function pointer.
            
    Returns:
        Returns the list of calls for the function on stack.

    Raises:
        passed through exceptions:

    """    
    _sl = inspect.stack()
    _r = {}
    for _s in _sl:

        t0 = type(funp)
        t1 = type(_s)
        
        if funp == _s[0]:
            _r[_sl.index(_s)] = funp
        elif type(funp) != type(_s) and ismethod(funp):
            if _s[3] == funp.__name__:
                _r[_sl.index(_s)] = funp
        elif type(funp) != type(_s) and ismethod(_s):
            if _s[3] == funp[3]:
                _r[_sl.index(_s)] = funp
        
    return _r 

def getStackFuncNameMap(fun):
    """Returns a list of funcnames for each call of func on the stack.

    Args:
        fun: Function name as regexpr.
            
    Returns:
        Returns the list of function names on stack.

    Raises:
        passed through exceptions:

    """    
    _c = re.compile(fun)
    _sl = inspect.stack()
    _r = {}
    for _s in _sl:
        if _c.match(_s[3]):
            _r[_sl.index(_s)] = _s[3] 
    return _r 

def getStackLen():
    """Returns the length of current stack.

    Args:

    Returns:
        Returns the len of current stack.

    Raises:
        passed through exceptions:
    """
    return len(inspect.stack())

def getStackSposForFunc(funp):
    """Returns the id:=mem-address of the caller function.

    The ID is independent over of the call context during
    it's lifetime.

    Args:
        funp: Function on current stack.

    Returns:
        Returns the spos.

    Raises:
        passed through exceptions:

    """
    _sl = inspect.stack()
    for _s in _sl:
        if funp == _s[0]:
            return _sl.index(_s) 
    return None

def getStackSposForFuncName(fun,fromtop=False):
    """Returns the current stack position(spos) of the function name.

    The position and it's content are specific to the call context.
    When fromtop==False, the position is 'almost' static - for the
    lifetime of the referenced object.
 
    Args:
        fun=(literal|regexpr): Caller function name on the stack.
            literal: a literal name
            regexpr: a regular expression for 're'

        fromtop: If True, return the value as a topdown index for
            the current stack, thus negative/<0.
            
            default:=False

    Returns:
        Returns the spos, for loops and validation use:

            fromtop==False:   result >=0

            fromtop==True:    result <0

    Raises:
        passed through exceptions:

    """
    _c = re.compile(fun)
    _st = inspect.stack()
    if fromtop:
        _st = reversed(_st)
    for _s in _st:
        if _c.match(_s[3]):
            return _st.index(_s) 
    return -1

