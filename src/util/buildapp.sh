#!/usr/bin/env bash
MYDIR="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
SRCROOT=${MYDIR%/*}
MD=$1

       NAME=`cat $MD | awk 'match($0,/##NAME## .*/) { print substr($0,RSTART+9,RLENGTH-10)}'`
DESCRIPTION=`cat $MD | awk 'match($0,/##DESCRIPTION## .*/) { print substr($0,RSTART+16,RLENGTH-17)}'`
    APICALL=`cat $MD | awk 'match($0,/##APICALL## .*/) { print substr($0,RSTART+12,RLENGTH-13)}'`

cat $SRCROOT/templates/header.1.html.template | sed "s/##DESCRIPTION##/$DESCRIPTION/"
$MYDIR/buildmenu.sh aplikace
cat $SRCROOT/templates/header.2.html.template
$MYDIR/md2html.py $MD
echo "<script>"
cat $SRCROOT/templates/apps.js.template | sed "s/##APICALL##/$APICALL/"
echo "</script>"
cat $SRCROOT/templates/footer.1.html.template
cat $SRCROOT/templates/footer.2.html.template
