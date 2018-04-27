import os
import boto3
from io import BytesIO
import zipfile



def lambda_handler(event, context):
    """
    Downloads zip from build bucket, and extracts to deploy bucket
    """
    
    s3 = boto3.resource('s3')
    build_bucket = s3.Bucket(os.environ['SOURCE_BUCKET'])
    deploy_bucket = s3.Bucket(os.environ['TARGET_BUCKET'])


    #build_zip = StringIO.StringIO()
    if not zip_fileref:
        zip_fileref = BytesIO()
    build_bucket.download_fileobj('slsbuild.zip', zip_fileref)

    # now upload
    with zipfile.ZipFile(zip_fileref) as myzip:
        for nm in myzip.namelist():
            obj = myzip.open(nm)
            deploy_bucket.upload_fileobj(obj, nm)
            deploy_bucket.Object(nm).Acl().put(ACL='public-read')

    
    return 'Copied Code from one bucket to another'

