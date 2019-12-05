pysourceinfo
============

The 'pysourceinfo' package provides basic runtime information on executed 
sourcefiles and modules based on 'inspect', 'sys', 'os', and additional sources.
The covered objects include packages, modules/files and functions/methods/scripts. 

**Online documentation**:

* https://pysourceinfo.sourceforge.io/

**Runtime-Repository**:

* PyPI: https://pypi.org/project/pysourceinfo/

  Install: *pip install pysourceinfo*, see also 'Install'.

**Downloads**:

* bitbucket.org: https://bitbucket.org/acue/pysourceinfo

* github.com: https://github.com/ArnoCan/pysourceinfo/

* pypi.org: https://pypi.org/project/pysourceinfo/

* sourceforge.net: https://sourceforge.net/projects/pysourceinfo/files/

Project Data
------------

* PROJECT: 'pysourceinfo'

* MISSION: Support easy access to RTTI for Python source and binary files.

* VERSION: 00.01

* RELEASE: 00.01.038

* STATUS: alpha

* AUTHOR: Arno-Can Uestuensoez

* COPYRIGHT: Copyright (C) 2010,2011,2015-2019 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez

* LICENSE: Artistic-License-2.0 + Forced-Fairplay-Constraints

Concepts and enumeration values are migrated from the 

* *UnifiedSessionsManager* (C) 2008 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez.  

Runtime Environment
-------------------
For a comprehensive list refer to the documentation.

**Python Syntax Support**

*  Python2.7, and Python3

**Python Implementation Support**

*  CPython, IPython, IronPython, Jython, and PyPy

**OS on Server, Workstation, Laptops, Virtual Machines, and Containers**

* Linux: AlpineLinux, ArchLinux, CentOS, Debian, Fedora, Gentoo, OpenSUSE, Raspbian, RHEL, Slackware, SLES, Ubuntu, ...  

* BSD: DragonFlyBSD, FreeBSD, NetBSD, OpenBSD, GhostBSD, TrueOS, NomadBSD

* OS-X: Snow Leopard

* Windows: Win10, Win8.1, Win7, WinXP, Win2019, Win2016, Win2012, Win2008, Win2000

* WSL-1.0: Alpine, Debian, KaliLinux, openSUSE, SLES, Ubuntu

* Cygwin

* UNIX: Solaris10, Solaris11

* Minix: Minix3

* ReactOS

**Network and Security**

* Network Devices: OpenWRT

* Security: KaliLinux, pfSense, BlackArch, ParrotOS, Pentoo

**OS on Embedded Devices**

* RaspberryPI: ArchLinux, CentOS, OpenBSD, OpenWRT, Raspbian

* ASUS-TinkerBoard: Armbian

Current Release
---------------

Major Changes:

* Minor fixes

* extended *helper.getpythonpath*, and *helper.getpythonpath_rel*

* added *helper.getpythonpath_rel_oid*

* added support for Python3.x

* added support for various Python implementations

* additionally tested on various Linux, BSD, Windows, see documents section 'Install'

* Changed to *ReadTheDocs* as he the default template for the documentation

* Added API reference documentation by Epydoc 

ToDo:

* AIX

* MicroPython, CircuitPython

* test OpenBSD on rpi3

* test Windows10IoT-Core

