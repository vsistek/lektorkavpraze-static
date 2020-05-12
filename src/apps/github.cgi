#!/bin/bash

REPO=/var/www/lektorkavpraze-static

json_resp() {
     echo "Content-type: text/json"
     echo ""
     echo '{"result":"'"$([[ $1 -eq 0 ]] && echo "success" || echo "failure")"'"}'
     exit 0
}

POSTJSON="$(cat -)"

EXPECTEDURL="https://github.com/vsistek/lektorkavpraze-static.git"
REPOURL="$(jq -r ".repository.clone_url" <<< "$POSTJSON")"
[ "$EXPECTEDURL" == "$REPOURL" ] || json_resp 1

REF="$(jq -r ".ref" <<< "$POSTJSON")"
BRANCH="${REF##*/}"

if [ "$BRANCH" == "master" ] && [ "$(hostname)" == "skyholm" ]; then
    $REPO/src/util/deploy.sh >/dev/null
elif [ "$BRANCH" == "dev" ] && [ "$(hostname)" == "duthac.sistkovi.cz" ]; then
    $REPO/src/util/deploy-dev.sh >/dev/null
fi

json_resp 0
