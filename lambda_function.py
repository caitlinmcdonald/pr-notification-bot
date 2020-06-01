import json
import os
from botocore.vendored import requests
from slack import WebClient
from slack.errors import SlackApiError

def lambda_handler(event, context):
  # setup url
    repo_info = event['repository']
    pr_url = repo_info['html_url'] + "/pulls"
    
    # setup bot communication
    BOT_NAME = 'slack-bot-tutorial'
    SLACK_BOT_TOKEN = os.environ['SLACK_BOT_TOKEN']
    client = WebClient(token=SLACK_BOT_TOKEN)
    
    # send slack message to designated channel
    try: response = client.chat_postMessage(
        channel = 'test-bot',
        block = [
            {
                'type': 'section',
                'text': {
                    'type': 'mrkdwn',
                    'text': '*Quick PR for review*\nPlease check it out <pr_url|here.>'
                }
            },
            {
                'type': 'divider'
            }
            ]
        )
    except SlackApiError as e:
        # you get a SlackApiError if "ok" is false
        assert e.response['error']
        
    # return successful status code and basic info
    return {
        'statusCode': 200,
        'body': json.dumps(pr_url)
    }
