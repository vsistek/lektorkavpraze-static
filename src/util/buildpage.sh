#!/usr/bin/env bash
export LANG=C.UTF-8

MYDIR="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
SRCROOT=${MYDIR%/*}
MD=$1

       NAME=`cat $MD | awk 'match($0,/##NAME## .*/) { print substr($0,RSTART+9,RLENGTH-10)}'`
DESCRIPTION=`cat $MD | awk 'match($0,/##DESCRIPTION## .*/) { print substr($0,RSTART+16,RLENGTH-17)}'`
      QUOTE=`cat $MD | awk 'match($0,/##QUOTE## .*/) { print substr($0,RSTART+10,RLENGTH-11)}'`

cat $SRCROOT/templates/header.1.html.template | sed "s/##DESCRIPTION##/$DESCRIPTION/"
$MYDIR/buildmenu.sh $NAME
cat $SRCROOT/templates/header.2.html.template
$MYDIR/md2html.py $MD
cat $SRCROOT/templates/footer.1.html.template
[ $QUOTE == "none" ] || cat $SRCROOT/templates/quote.html.template | sed "s/##QUOTE##/$QUOTE/"
cat $SRCROOT/templates/footer.2.html.template
