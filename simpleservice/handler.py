"""
handler.py

author: matt cliff
created: april 16, 2018

AWS lambda python 3.6 code

Creates generic Lambda function that logs the event and context
- has API Gateway triggers for GET/POST
  
"""
import os
import datetime
import json
import logging
from decimal import Decimal


LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)



def handle_service(event, context):
    """
    used for debugging
    """
    logging.info("debug: event: %s", event)
    logging.info("debug: context: %s", context)

    #operation = event['httpMethod']
    #data = event['queryStringParameters'] if operation == 'GET' else json.loads(event['body'])
    
    return {
        "body": json.dumps(event),
        "headers": {
            "Content-Type" : "application/json",
        },
    }

