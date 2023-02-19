#!/bin/bash

LOG=/var/www/lektorkavpraze-cz/log/github.log

# github is unhappy when we don't read the payload
cat - > /dev/null

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

date >> $LOG
[ `hostname` == "laputa" ] || json_resp 1
/var/www/lektorkavpraze-cz/src/util/deploy.sh >> $LOG 2>&1
json_resp 0
