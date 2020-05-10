#!/usr/bin/env bash
export LANG=C.UTF-8

LOCKFILE=/var/www/lektorkavpraze-static/lock/just-deployed

echo "Content-Type: text/plain; charset=utf-8"
echo
find $LOCKFILE -mmin +5 2>/dev/null
[ $? -ne 0 ] && rm $LOCKFILE
[ -f $LOCKFILE ] && echo "try later" && exit 0
echo mkdir log
mkdir -p /var/www/lektorkavpraze-static/log
echo mkdir lock
mkdir -p /var/www/lektorkavpraze-static/lock
cd /var/www/lektorkavpraze-static
echo git pull
git pull
echo src/util/build.sh
/var/www/lektorkavpraze-static/src/util/build.sh
echo refresh lock
touch $LOCKFILE

