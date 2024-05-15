import json

def lambda_handler(event, context):
    
    return {
        'statusCode': 200,
        'body': json.dumps('Session 12 of D4C Course!')
    }