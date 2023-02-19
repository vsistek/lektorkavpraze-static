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
    echo "}"
    exit 0
}

POSTJSON=`cat -`
date >> $LOG

REPOURL=`jq -r ".repository.clone_url" <<< $POSTJSON`
echo "EXPECTEDURL=$EXPECTEDURL / REPOURL=$REPOURL" >> $LOG
[ "$EXPECTEDURL" == "$REPOURL" ] || json_resp 1
[ `hostname` == "laputa" ] || json_resp 1
$REPO/src/util/deploy.sh >> $LOG 2>&1
json_resp 0
