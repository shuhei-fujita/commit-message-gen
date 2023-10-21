#!/bin/bash
COMMIT_MSG_FILE=$1
COMMIT_MSG=$(bash -c "export VIRTUAL_ENV=$(poetry env info --path) && $VIRTUAL_ENV/bin/python /Users/shuhei/git/commit-message-gen/script.py")
echo "$COMMIT_MSG" > $COMMIT_MSG_FILE
