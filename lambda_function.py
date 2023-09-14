# This program prints Hello, world!
# print('Hello, world!')
import json

def lambda_handler(event, context):
    # TODO implement
    return {
            'statusCode': 200,
            'body': json.dumps('Welcome to MFH')
           }
