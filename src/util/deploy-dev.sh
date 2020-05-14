#!/usr/bin/env bash

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
