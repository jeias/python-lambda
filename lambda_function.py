import json


def lambda_handler(event, context):
    # TODO implement

    print("body -> " + event.get('body'))
    print("direct message ->" + event.get('message'))

    return {
        'statusCode': 200,
        'body': json.dumps({'top': "eu"})
    }
