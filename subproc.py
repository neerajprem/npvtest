import json
import requests

SlackMessage = "testing emoji codes :simple_smile: "
webhook_url = 'https://hooks.slack.com/services/XYXYXYXYXY/ABCDEFGHI/123456789012345678901234'
slack_data = {'text': SlackMessage }

response = requests.post( webhook_url, data=json.dumps(slack_data), headers={'Content-Type': 'application/json'})
print response

if response.status_code != 200:
    raise ValueError(
        'Request to slack returned an error %s, the response is:\n%s'
        % (response.status_code, response.text)
    )