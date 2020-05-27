import json

def lambda_handler(event, context):
  return {
    "statusCode": 200,
    "body": JSON.stringify('Hello from Lambda and GitHub!')
  }
