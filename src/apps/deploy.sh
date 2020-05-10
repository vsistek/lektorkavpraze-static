#!/usr/bin/env bash
export LANG=C.UTF-8

echo "Content-Type: text/plain; charset=utf-8"
echo
cd /var/www/lektorkavpraze-static
echo git pull
git pull
echo src/util/build.sh
/var/www/lektorkavpraze-static/src/util/build.sh
