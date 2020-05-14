#!/bin/bash

REPO=/var/www/lektorkavpraze-static

json_resp() {
    echo "Content-type: text/json"
    echo
    if [ $1 -eq 0 ]; then
        echo "{\"result\":\"success\","
    else
        echo "{\"result\":\"failure\","
    fi
    echo " \"branch\":\"$BRANCH\","
    echo " \"hostname\":\"$HOSTNAME\""
    echo " \"buildcmd\":\"$BUILDCMD\""
    echo "}"
    exit 0
}

POSTJSON=`cat -`
BUILDCMD="none"
LOG=$REPO/log/github.log
echo "---" >> $LOG
date >> $LOG
echo "POSTJSON=$POSTJSON" >> $LOG

EXPECTEDURL="https://github.com/vsistek/lektorkavpraze-static.git"
echo "EXPECTEDURL=$EXPECTEDURL" >> $LOG
REPOURL=`jq -r ".repository.clone_url" <<< $POSTJSON`
echo "REPOURL=$REPOURL" >> $LOG
[ "$EXPECTEDURL" == "$REPOURL" ] || json_resp 1

REF=$(jq -r ".ref" <<< "$POSTJSON")
echo "REF=$REF" >> $LOG
BRANCH="${REF##*/}"
echo "BRANCH=$BRANCH" >> $LOG
HOSTNAME=$(hostname)
echo "HOSTNAME=$HOSTNAME" >> $LOG

[ "$BRANCH" == "master" ] && [ "$HOSTNAME" == "skyholm" ]            && BUILDCMD="deploy"
[ "$BRANCH" == "dev" ]    && [ "$HOSTNAME" == "duthac.sistkovi.cz" ] && BUILDCMD="deploy-dev"

[ "$BUILDCMD" == "none" ] && json_resp 0
$REPO/src/util/$BUILDCMD.sh >> $LOG 2>&1

json_resp 0
