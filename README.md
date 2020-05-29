# prNotificationBot
slack bot

1. PR gets created
2. Webhook sends payload to AWS Rest API Gateway
3. Gateway invokes AWS Lambda function
4. Function parses payload and retrieves GitHub URL associated to PR
5. Function sends slack channel message with URL
