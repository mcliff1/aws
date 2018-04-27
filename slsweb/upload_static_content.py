import os
import boto3
from io import BytesIO
import zipfile

def lambda_handler(event, context):
    """
    Downloads zip from build bucket, and extracts to deploy bucket
    """

    sns = boto3.resource('sns')
    topic = sns.Topic(os.environ['SNS_TOPIC'])

    try:    
        s3 = boto3.resource('s3')
        build_bucket = s3.Bucket(os.environ['SOURCE_BUCKET'])
        deploy_bucket = s3.Bucket(os.environ['TARGET_BUCKET'])

        if not zip_fileref:
            zip_fileref = BytesIO()
        build_bucket.download_fileobj(os.environ['BUILD_PACKAGE'], zip_fileref)

        # now upload
        with zipfile.ZipFile(zip_fileref) as myzip:
            for nm in myzip.namelist():
                obj = myzip.open(nm)
                deploy_bucket.upload_fileobj(obj, nm)
                deploy_bucket.Object(nm).Acl().put(ACL='public-read')


        topic.publish(Subject="SLS Portfolio Deployed", Message="Portfolio successfully deployed")
    except:
        topic.publish(Subject="SLS Deployment Failed", Message="Portfolio successfully deployed")
        raise
    
    return 'Copied Code from one bucket to another'

