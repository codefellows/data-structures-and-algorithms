#!/bin/bash

echo "Getting Code Challenge $1"

`which curl` -s https://codefellows.github.io/code-301-guide/curriculum/class-$1/challenges/challenges-$1.test.js > ./code-challenges/challenges-$1.test.js
