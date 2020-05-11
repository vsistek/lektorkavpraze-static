#!/usr/bin/env bash
export LANG=C.UTF-8

echo "Content-Type: application/json; charset=utf-8"
echo
[ -e $QUERY_STRING.yaml ] && python3 genrandomtask.py $QUERY_STRING.yaml 
