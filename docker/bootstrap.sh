#!/bin/bash
date
ls
# if the bucket exists list it, else make it
aws s3 ls $CI_BUCKET > /dev/null 2> /dev/null || aws s3 mb s3://$CI_BUCKET
aws sts get-caller-identity

echo "Stack name is $STACK_NAME"

echo "params are $@"

# run aws create-stack with / ???
# check to see if the bucket exists

#  or maybe instead run SAM command ???
sam validate

sam package --template-file template.yaml --s3-bucket ${CI_BUCKET} --s3-prefix=${STACK_NAME} --output-template-file interim-template-file.yaml

sam deploy --paramater-overrides Hostname=${STACK_NAME} --template-file interim-template-file.yaml --stack-name=${STACK_NAME} --capabilities CAPABILITY_IAM
