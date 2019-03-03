"""
index.py

author: matt cliff
created: March 2, 2019

AWS lambda python 3.6 code

Will provide a simple UI through Lambda
"""
import os
import logging


LOGGER = logging.getLogger()
LOGGER.setLevel(logging.DEBUG)



def handle(event, context):
    """
    used for debugging
    """
    logging.debug('debug: event: %s', event)

    return {
        'body': json.dumps(event),
        'headers': {
            'Content-Type': 'application/json'
        }
    }
