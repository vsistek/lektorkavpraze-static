#!/usr/bin/env bash

LOCKFILE=/var/www/lektorkavpraze-static/lock/just-deployed

[ `find $LOCKFILE -mmin +1 2>/dev/null |wc -l` -ne 0 ] && rm $LOCKFILE
[ -f $LOCKFILE ] && echo "try later" && exit 0
echo mkdir log
mkdir -p /var/www/lektorkavpraze-static/log
echo mkdir lock
mkdir -p /var/www/lektorkavpraze-static/lock
cd /var/www/lektorkavpraze-static
echo git pull
git pull
echo git checkout dev
git checkout dev
echo src/util/build.sh
/var/www/lektorkavpraze-static/src/util/build.sh
echo refresh lock
touch $LOCKFILE
