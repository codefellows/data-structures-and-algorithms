#!/bin/bash

echo "Getting Code Challenge $1"

`which curl` -s https://rfro9k76xg.execute-api.us-west-2.amazonaws.com/default/getCodeChallenge?challenge=$1 > ./code-challenges/challenges-$1.test.js
