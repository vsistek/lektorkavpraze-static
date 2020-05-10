#!/usr/bin/env bash
DOCROOT=/var/www/lektorkavpraze.cz/htdocs
MYDIR="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
SRCROOT=${MYDIR%/*}

mkdir -p $DOCROOT

for MD in `ls $SRCROOT/*.md`; do
    MD=${MD##*/}
    FILE=$DOCROOT/${MD:3:-3}.html
    echo $FILE
    $MYDIR/buildpage.sh $SRCROOT/$MD > $FILE
done

mkdir -p $DOCROOT/styles
cp $SRCROOT/styles/*.css $DOCROOT/styles
ls -l $DOCROOT/styles/*.css
mkdir -p $DOCROOT/images
cp $SRCROOT/images/*.png $DOCROOT/images
ls -l $DOCROOT/images/*.png

mkdir -p $DOCROOT/aplikace
for MD in `ls $SRCROOT/apps/*.md`; do
    MD=${MD##*/}
    FILE=$DOCROOT/aplikace/${MD:0:-3}.html
    echo $FILE
    $MYDIR/buildapp.sh $SRCROOT/apps/$MD > $FILE
done

cp $SRCROOT/apps/*.yaml $DOCROOT/aplikace
ls -l $DOCROOT/aplikace/*.yaml
cp $SRCROOT/apps/*.sh $DOCROOT/aplikace
ls -l $DOCROOT/aplikace/*.sh
chmod +x $DOCROOT/aplikace/*.sh
cp $SRCROOT/apps/*.py $DOCROOT/aplikace
ls -l $DOCROOT/aplikace/*.py
