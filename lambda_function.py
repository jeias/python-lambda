import json


def lambda_handler(event, context):
    # TODO implement

    print("body -> " + event.get('body', 'FUDEU'))
    print("direct message ->" + event.get('FUDEU'))

    return {
        'statusCode': 200,
        'body': json.dumps({'top': "eu"})
    }
