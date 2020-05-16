#!/usr/bin/env bash
MYDIR="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
SRCROOT=${MYDIR%/*}
DOCROOT="${SRCROOT%/*}/htdocs"

fail() {
    echo $1
    exit 1
}

mkdir -p $DOCROOT

for MD in `ls $SRCROOT/*.md`; do
    TMP=${MD##*-}
    FILE=$DOCROOT/${TMP%.md}.html
    echo $FILE
    $MYDIR/buildpage.sh $MD > $FILE || fail "page build error for $MD"
done

mkdir -p $DOCROOT/styles
cp $SRCROOT/styles/*.css $DOCROOT/styles
ls -l $DOCROOT/styles/*.css
mkdir -p $DOCROOT/images
cp $SRCROOT/images/*.png $DOCROOT/images
cp $SRCROOT/images/*.webp $DOCROOT/images
ls -l $DOCROOT/images/

mkdir -p $DOCROOT/aplikace
for MD in `ls $SRCROOT/apps/*.md`; do
    TMP=${MD##*/}
    FILE=$DOCROOT/aplikace/${TMP%.md}.html
    echo $FILE
    $MYDIR/buildapp.sh $MD > $FILE
done

cp $SRCROOT/apps/*.yaml $DOCROOT/aplikace
cp $SRCROOT/apps/*.cgi $DOCROOT/aplikace
chmod +x $DOCROOT/aplikace/*.cgi
cp $SRCROOT/apps/*.py $DOCROOT/aplikace
cp $SRCROOT/apps/*.conf $DOCROOT/aplikace
ls -l $DOCROOT/aplikace/
