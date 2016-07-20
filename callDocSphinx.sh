PROJECT='pysourceinfo'
VERSION="0.1.5"
RELEASE="0.1.5"
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

# input base directory
INDIR=${INDIR:-$MYPATH}
if [ "X${INDIR#.}" != "X$INDIR" ];then
	INDIR=${PWD}/${INDIR#.};INDIR=${INDIR//\/\//\/}
fi

echo "MYPATH=$MYPATH"
echo "INDIR=$INDIR"
 
# output base directory
OUTDIR=${OUTDIR:-build/}
if [ ! -e "${OUTDIR}" ];then
	mkdir -p "${OUTDIR}"
fi
export PYTHONPATH=$PWD:$MYPATH:$PYTHONPATH

# import directory for entries of static reference 
STATIC="${OUTDIR}/apidoc/sphinx/_static"

# source entities
FILEDIRS=""
FILEDIRS="${INDIR}dosrc"
FILEDIRS="$FILEDIRS ${INDIR}pysourceinfo"
FILEDIRS="$FILEDIRS ${INDIR}UseCases"
FILEDIRS="$FILEDIRS ${INDIR}tests"
FILEDIRS="$FILEDIRS ${INDIR}testdata"

#FILEDIRS="$FILEDIRS ${INDIR}setup.py"
#FILEDIRS="$FILEDIRS ${INDIR}bin"

CALL=""
CALL="$CALL export PYTHONPATH=$PWD:$MYPATH:$PYTHONPATH;"
CALL="$CALL sphinx-apidoc "
CALL="$CALL -A '$AUTHOR'"
CALL="$CALL -H '$PROJECT'"
CALL="$CALL -V '$VERSION'"
CALL="$CALL -R '$RELEASE'"
CALL="$CALL -o ${OUTDIR}/apidoc/sphinx"
CALL="$CALL -f -F "
CALL="$CALL $@"

#
DOCHTMLDIR=${OUTDIR}apidoc/sphinx/_build/
DOCHTML=${DOCHTMLDIR}html/index.html
cat <<EOF
#
# Create apidoc builder...
#
EOF
IFSO=$IFS
IFS=';'
FX=( ${FILEDIRS} )
IFS=$IFSO
for fx in ${FX[@]};do
	echo "CALL=<$CALL '$fx'>"
	eval $CALL "$fx"
done

# echo "extensions.append('sphinx.ext.intersphinx.')" >> ${OUTDIR}/apidoc/sphinx/conf.py
# echo "sys.path.insert(0, os.path.abspath('$PWD/..'))" >> ${OUTDIR}/apidoc/sphinx/conf.py
{
cat <<EOF 

extensions.append('sphinx.ext.intersphinx.')
sys.path.insert(0, os.path.abspath('$PWD/..'))

html_logo = "_static/pysourceinfo-64x64.png"
#html_favicon = None

#html_theme = "classic"
#html_theme = "pyramid"
#html_theme = "agogo"
#html_theme = "bizstyle"
html_theme_options = {
#    "rightsidebar": "true",
#    "relbarbgcolor": "black",
    "externalrefs": "true",
    "sidebarwidth": "290",
    "stickysidebar": "true",
#    "collapsiblesidebar": "true",

#    "footerbgcolor": "",
#    "footertextcolor": "",
#    "sidebarbgcolor": "",
#    "sidebarbtncolor": "",
#    "sidebartextcolor": "",
#    "sidebarlinkcolor": "",
#    "relbarbgcolor": "",
#    "relbartextcolor": "",
#    "relbarlinkcolor": "",
#    "bgcolor": "",
#    "textcolor": "",
#    "linkcolor": "",
#    "visitedlinkcolor": "",
#    "headbgcolor": "",
#    "headtextcolor": "",
#    "headlinkcolor": "",
#    "codebgcolor": "",
#    "codetextcolor": "",
#    "bodyfont": "",
#    "headfont": "",

}

# def setup(app):
#     app.add_stylesheet('css/custom.css')

EOF
} >> ${OUTDIR}/apidoc/sphinx/conf.py
mkdir "${STATIC}/css/"
cp docsrc/custom.css "${STATIC}/css/custom.css"
cp docsrc/pysourceinfo-64x64.png "${STATIC}/"


# put the docs together
#
cat docsrc/index.rst                     > ${OUTDIR}/apidoc/sphinx/index.rst
{
cat <<EOF
Project data summary:

* PROJECT=${PROJECT}

* MISSION=${MISSION}

* AUTHOR=${AUTHOR}

* COPYRIGHT=${COPYRIGHT}

* LICENSE=${LICENSE}

* VERSION=${VERSION}

* RELEASE=${RELEASE}

* STATUS=${STATUS}

* NICKNAME=${NICKNAME}

  Internal information on the Python call stack by ${NICKNAME}, see \`${NICKNAME}
  - located beneath the world tree Yggdrasil, the water of the well
  contains much wisdom, and Odin's eye sacrifice to the well was in exchange
  for a drink from it...
  <https://en.wikipedia.org/wiki/Mimisbrunnr>\`_  

EOF
} >> ${OUTDIR}/apidoc/sphinx/index.rst 

#
cat docsrc/sourceinfo.rst > ${OUTDIR}/apidoc/sphinx/sourceinfo.rst
cat docsrc/pysourceinfo.rst > ${OUTDIR}/apidoc/sphinx/pysourceinfo.rst
cat docsrc/shortcuts.rst > ${OUTDIR}/apidoc/sphinx/shortcuts.rst
#
# static - literal data
cat ArtisticLicense20.html > "${STATIC}/ArtisticLicense20.html"
cat licenses-amendments.txt > "${STATIC}/licenses-amendments.txt"
#
#cp docsrc/lionwhisperer.png "${STATIC}"

#CALL="SPHINXOPTS= "
CALL=" "
#CALL="SPHINXBUILD=sphinx-build PYTHONPATH=$PYTHONPATH "
CALL="export SPHINXBUILD=sphinx-build; "
CALL="$CALL cd ${OUTDIR}/apidoc/sphinx;"
#CALL="$CALL export PYTHONPATH=$PYTHONPATH "
CALL="$CALL export PYTHONPATH=$PWD:$MYPATH:$PYTHONPATH;"
#CALL="$CALL export PYTHONPATH=$PYTHONPATH; "
CALL="$CALL make html ;"
CALL="$CALL cd - "
cat <<EOF
#
# Build apidoc...
#
EOF
echo "CALL=<$CALL>"
eval $CALL

# docdir
DOCDIR="${DOCDIR:-doc/en/html/man3/$PROJECT}"
if [ ! -e "${DOCDIR}" ];then
	mkdir -p "${DOCDIR}"
fi
cp -a "${DOCHTMLDIR}"/html/* "${DOCDIR}"
echo
echo "display with: firefox -P preview.simple ${DOCHTML}"
echo "display with: firefox -P preview.simple ${DOCDIR}/index.html"
echo
