import json


def lambda_handler(event, context):
    # TODO implement

    print(event['key1'])

    return {
        'statusCode': 200,
        'body': event['key1']
    }
