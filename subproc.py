import json
import requests

webhook_url = 'https://hooks.slack.com/services/XYXYXYXYXY/ABCDEFGHI/123456789012345678901234'
slack_data = {'text': "My Pyhton code to send messages to Slack's incoming webhook is working"}

response = requests.post( webhook_url, data=json.dumps(slack_data), headers={'Content-Type': 'application/json'})
print response

if response.status_code != 200:
    raise ValueError(
        'Request to slack returned an error %s, the response is:\n%s'
        % (response.status_code, response.text)
    )