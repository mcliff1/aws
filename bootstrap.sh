#!/bin/bash
#
# expects variables
#  SAM_BUCKET  - an s3 bucket that is used for build/deploy resources (can be shared with other SAM builds)
#  STACK_NAME  - name of the stack that will be created
#
#   HOSTNAME
#   DOMAINNAME
#   SSL CERT
#
date

# if the bucket exists list it, else make it
aws s3 ls $SAM_BUCKET > /dev/null 2> /dev/null || aws s3 mb s3://$SAM_BUCKET
aws sts get-caller-identity

echo "Stack name is $STACK_NAME"

# run aws create-stack with / ???
# check to see if the bucket exists

#  or maybe instead run SAM command ???
sam validate

sam package --template-file template.yaml --s3-bucket ${SAM_BUCKET} --s3-prefix=${STACK_NAME} --output-template-file ${HOME}/interim-template-file.yaml

echo STACK_NAME is $STACK_NAME
sam deploy --parameter-overrides Hostname=${STACK_NAME} --template-file interim-template-file.yaml --stack-name $STACK_NAME --capabilities CAPABILITY_IAM
