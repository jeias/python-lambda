import json

def lambda_handler(event, context):
    # TODO implement

    return {
        'statusCode': 200,
        'message': event['message']
    }
