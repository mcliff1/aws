#!/bin/bash
set -eu
REGION=${2:-us-east-1}
STAGE="${1:-dev}"
echo "Deploying static assets to ${STAGE}..."

BUCKET_NAME=$(aws \
    cloudformation describe-stacks \
    --region "${REGION}" \
    --stack-name "gladnews-${STAGE}" \
    --query "Stacks[0].Outputs[?OutputKey=='WebSiteBucket'] | [0].OutputValue" \
    --output text)

WEBSITE_URL=$(aws \
    cloudformation describe-stacks \
    --region "${REGION}" \
    --stack-name "gladnews-${STAGE}" \
    --query "Stacks[0].Outputs[?OutputKey=='WebSiteUrl'] | [0].OutputValue" \
    --output text)


aws s3 sync --region "${REGION}" --acl 'public-read' --delete ./static/ "s3://${BUCKET_NAME}/"

echo "Bucket URL: ${WEBSITE_URL}"

