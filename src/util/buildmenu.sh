#!/usr/bin/env bash
MYDIR="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
SRCROOT=${MYDIR%/*}

ACTIVE=$1

for MD in `ls $SRCROOT/*.md`; do
        NAME=`cat $MD | awk 'match($0,/##NAME## .*/) { print substr($0,RSTART+9,RLENGTH-10)}'`
    MENUITEM=`cat $MD | awk 'match($0,/##MENUITEM## .*/) { print substr($0,RSTART+13,RLENGTH-14)}'`

    if [ "$MENUITEM" != "none" ]; then
        LINE="<li><a "
        [ "$NAME" == "$ACTIVE" ] && LINE+="class=\"active\" "
        LINE+="href=\"/$NAME.html\">$MENUITEM</a></li>"
        echo "        $LINE"
    fi
done
