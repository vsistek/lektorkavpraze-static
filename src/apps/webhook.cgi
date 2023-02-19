#!/bin/bash

fail() {
    echo $1
    exit 1
}

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
source "$DIR/webhook.conf"
[ "$REPO" == "" ]        && fail "REPO undefined"
[ "$EXPECTEDURL" == "" ] && fail "EXPECTEDURL undefined"
[ "$LOG" == "" ]         && fail "LOG undefined"

json_resp() {
    echo "Content-type: text/json"
    echo
    if [ $1 -eq 0 ]; then
        echo "{\"result\":\"success\","
    else
        echo "{\"result\":\"failure\","
    fi
    echo " \"hostname\":\"$HOSTNAME\""
    echo " \"buildcmd\":\"$BUILDCMD\""
    echo "}"
    exit 0
}

POSTJSON=`cat -`
BUILDCMD="none"

date >> $LOG

REPOURL=`jq -r ".repository.clone_url" <<< $POSTJSON`
echo "EXPECTEDURL=$EXPECTEDURL / REPOURL=$REPOURL" >> $LOG
[ "$EXPECTEDURL" == "$REPOURL" ] || json_resp 1
HOSTNAME=`hostname`
echo "HOSTNAME=$HOSTNAME" >> $LOG

[ "$HOSTNAME" == "laputa" ] && BUILDCMD="deploy"

[ "$BUILDCMD" == "none" ] && json_resp 0
$REPO/src/util/$BUILDCMD.sh >> $LOG 2>&1

json_resp 0
