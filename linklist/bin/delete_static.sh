#!/bin/bash
set -eu

STAGE="${1:-dev}"
REGION=${2:-us-east-1}"

echo "You are about to DELETE ALL STATIC ASSETS from ${STAGE}"
echo "If that's not what you want, press ctrl-C to kill this script"
echo "Or press enter to continue"

read

echo "Deleting static assets from ${STAGE}..."

BUCKET_NAME=$(aws \
    cloudformation describe-stacks \
    --region "${REGION}" \
    --stack-name "gladnews-${STAGE}" \
    --query "Stacks[0].Outputs[?OutputKey=='WebSiteBucket'] | [0].OutputValue" \
    --output text)

mkdir /tmp/empty

aws s3 sync --region "${REGION}" --delete /tmp/empty/ "s3://${BUCKET_NAME}/"

rmdir /tmp/empty

echo "Bucket ${BUCKET_NAME} has been emptied"
