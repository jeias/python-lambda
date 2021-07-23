import json


def lambda_handler(event, context):
    # TODO implement

    coco = 'coco'

    if event['message']:
        coco = event['message']
    return {
        'statusCode': 200,
        'body': {
            'message': coco
        }
    }
