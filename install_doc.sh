PROJECT='pysourceinfo'
VERSION="0.1.2"
RELEASE="0.1.2"
NICKNAME="Mimisbrunnr"
AUTHOR='Arno-Can Uestuensoez'
COPYRIGHT='Copyright (C) 2010,2011,2015-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez'
LICENSE='Artistic-License-2.0 + Forced-Fairplay-Constraints'
STATUS='alpha'
MISSION='Support easy access to RTTI on Python source files.'

# the absolute pathname for this source
MYPATH=${BASH_SOURCE%/*}/
if [ "X${MYPATH#.}" != "X$MYPATH" ];then
	MYPATH=${PWD}/${MYPATH#.};MYPATH=${MYPATH//\/\//\/}
fi


#
DOCHTMLDIR=${OUTDIR}apidoc/sphinx/_build/
DOCHTML=${DOCHTMLDIR}html/index.html


#FIXME: see PEP 370 - Per user site-packages directory
#  Unix (including Mac) => ~/.local/doc 
#  Windows              => %APPDATA%/Python/doc
#
DOCDIR="doc/en/html/man3/$PROJECT"
TARGETDIR="${TARGETDIR:-$HOME/.local}/"
TARGETDIR="${TARGETDIR}doc/en/html/man3/"
if [ ! -e "${DOCDIR}" ];then
	${BASH_SOURCE%/*}/callDocSphinx.sh
fi
if [ ! -d ${TARGETDIR} ];then
	mkdir -p "${TARGETDIR}"
fi
cp -a "${DOCDIR}" "${TARGETDIR}"
echo
echo "display with: firefox -P preview.simple ${TARGETDIR}${PROJECT}/index.html"
if [ -e "${DOCDIR}.epydoc" ];then
	cp -a "${DOCDIR}.epydoc" "${TARGETDIR}"
	echo "display with: firefox -P preview.simple ${TARGETDIR}${PROJECT}.epydoc/index.html"
fi
echo
