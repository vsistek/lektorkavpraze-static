#!/usr/bin/env bash

LOCKFILE=/var/www/lektorkavpraze-cz/lock/just-deployed

[ `find $LOCKFILE -mmin +1 2>/dev/null |wc -l` -ne 0 ] && rm $LOCKFILE
[ -f $LOCKFILE ] && echo "try later" && exit 0
echo mkdir log
mkdir -p /var/www/lektorkavpraze-cz/log
echo mkdir lock
mkdir -p /var/www/lektorkavpraze-cz/lock
cd /var/www/lektorkavpraze-cz
echo git pull
git pull
echo src/util/build.sh
/var/www/lektorkavpraze-cz/src/util/build.sh
echo refresh lock
touch $LOCKFILE
