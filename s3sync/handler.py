"""
handler.py

author: matt cliff
created: july 11, 2018

AWS lambda python 3.6 code

Lambda function will sync two S3 repos;
expected environment variaoles:
SOURCE_BUCKET
TARGET_BUCKET
"""
import os
import logging


LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)

from awscli.clidriver import create_clidriver

"""
from https://github.com/boto/boto3/issues/358
expects to have awscli installed `pip install awscli`
"""
def aws_cli(*cmd):
    old_env = dict(os.environ)
    try:

        # Environment
        env = os.environ.copy()
        env['LC_CTYPE'] = u'en_US.UTF'
        os.environ.update(env)

        # Run awscli in the same process
        exit_code = create_clidriver().main(*cmd)

        # Deal with problems
        if exit_code > 0:
            raise RuntimeError('AWS CLI exited with code {}'.format(exit_code))
    finally:
        os.environ.clear()
        os.environ.update(old_env)


def handle_service(event, context):
    """
    used for debugging
    """
    logging.info("debug: event: %s", event)
    source = os.environ['SOURCE_BUCKET']
    target = os.environ['TARGET_BUCKET']

    logging.info("bucket properties source: %s, target: %s", source, target)
    aws_cli('s3', 'sync', source, target, '--delete')
    #operation = event['httpMethod']
    #data = event['queryStringParameters'] if operation == 'GET' else json.loads(event['body'])

    return {
        "body": json.dumps(event),
        "headers": {
            "Content-Type" : "application/json",
        }
    }
