#!/bin/bash
date
ls
# if the bucket exists list it, else make it
aws s3 ls $CI_BUCKET || aws s3 mb $CI_BUCKET
aws sts get-caller-identity

echo "Stack name is $STACK_NAME"

echo "params are $@"

# run aws create-stack with / ???
# check to see if the bucket exists

#  or maybe instead run SAM command ???
sam
