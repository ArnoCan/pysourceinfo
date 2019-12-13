# -*- coding: utf-8 -*-
"""Distribute 'sourceinfo', the core library for the display of information
about sources, modules, and packages.

Additional local options for this *setup.py* module:
   --sdk:
       Requires sphinx, epydoc, and dot-graphics.

   --no-install-requires: 
       Suppresses installation dependency checks,
       requires appropriate PYTHONPATH.

   --offline: 
       Sets online dependencies to offline, or ignores online
       dependencies.

"""
from __future__ import absolute_import
from __future__ import print_function

import os
import sys

import setuptools


__author__ = 'Arno-Can Uestuensoez'
__author_email__ = 'acue_sf2@sourceforge.net'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2015-2019 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__uuid__ = 'efed42d3-f801-4fbb-abfd-bd598d683a82'

__vers__ = [0, 1, 40,]
__version__ = "%02d.%02d.%03d"%(__vers__[0],__vers__[1],__vers__[2],)
__release__ = "%d.%d.%d" % (__vers__[0], __vers__[1], __vers__[2],) + '-rc0'
__status__ = 'beta'


__sdk = False
"""Set by the option "--sdk". Controls the installation environment."""
if '--sdk' in sys.argv:
    __sdk = True
    sys.argv.remove('--sdk')


# required for various interfaces, thus just do it
_mypath = os.path.dirname(os.path.abspath(__file__))
"""Path of this file."""
sys.path.insert(0, os.path.abspath(_mypath))


_name = 'sourceinfo'
"""package name"""

__pkgname__ = _name
"""package name"""

_version = "%d.%d.%d" % (__vers__[0], __vers__[1], __vers__[2],)
"""assembled version string"""

_install_requires = [
    'pythonids >=0.1.30',
]


_packages = ['sourceinfo',]
_packages_sdk = _packages

if __sdk:  # pragma: no cover
    try:
        import sphinx_rtd_theme  # @UnusedImport
    except:
        sys.stderr.write(
            "WARNING: Cannot import package 'sphinx_rtd_theme', cannot create local 'ReadTheDocs' style.")

    _install_requires.extend(
        [
            'sphinx >= 1.4',
            'epydoc >= 3.0',
        ]
    )

    _packages = _packages_sdk


__no_install_requires = False
if '--no-install-requires' in sys.argv:
    __no_install_requires = True
    sys.argv.remove('--no-install-requires')

__offline = False
if '--offline' in sys.argv:
    __offline = True
    __no_install_requires = True
    sys.argv.remove('--offline')


if __no_install_requires:
    print("#")
    print("# Changed to offline mode, ignore install dependencies completely.")
    print("# Requires appropriate PYTHONPATH.")
    print("# Ignored dependencies are:")
    print("#")
    for ir in _install_requires:
        print("#   " + str(ir))
    print("#")
    _install_requires = []


#
# see setup.py for remaining parameters
#
setuptools.setup(
    author=__author__,
    author_email=__author_email__,
    description="Utilities for simplified gain of runtime information on source code and binary locations.",
    download_url="https://sourceforge.net/projects/sourceinfo/files/",
    install_requires=_install_requires,
    license=__license__,
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    name=_name,
    packages=_packages,
    scripts=[],
    url='https://sourceforge.net/projects/sourceinfo/',
    version=_version,
    zip_safe=False,
)

sys.exit(0)

