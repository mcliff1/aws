#!/usr/bin/env bash
#
# script that will remove all delete markers from the specific Bucket and optional Prefix
#
# REF: https://stackoverflow.com/questions/32106094/how-to-remove-delete-markers-from-multiple-objects-on-amazon-s3-at-once
BUCKET=$1
PREFIX=$2


if [ "x$PREFIX" != "x" ]; then
  PREFIX_PARAM="--prefix $PREFIX"
fi


aws s3api list-object-versions --bucket $BUCKET $PREFIX_PARAM --output text | \
grep "DELETEMARKERS" | \
while read OBJ
do
  KEY=$( awk 'BEGIN{FS="\t"}{print $3}' <<< $OBJ )
  VERSION_ID=$( awk 'BEGIN{FS="\t"}{print $5}' <<< $OBJ )
  #VERSION_ID=$( echo $OBJ | awk '{print $5}')
  aws s3api delete-object --bucket $BUCKET --key "$KEY" --version-id $VERSION_ID
done
