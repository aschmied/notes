import json


def hello(event, context):
    response = {
        "statusCode": 200,
        "body": "42\n"
    }

    return response
