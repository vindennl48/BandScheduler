import json
import requests


# Send a notification to Slack via webhook
def notify(practice_info):
    payload = craft_payload(practice_info)
    send_push_notification(payload)

# Info contains the array of practice data, including the day of the week and
# location. Returns the JSON payload of the notification.
def craft_payload(info):
    message = 'Next practice will be in {0} on {1}'.format(info['Location'].title(), info['Day'].title())
    json_string = json.dumps({'text': message})

    return json_string

# Sends the request to the specified Slack webhook endpoint. If the request
# fails, an error is raised.
def send_push_notification(json):
    # should be noted that publishing this to github is probably not the most awesome idea.
    # that said, we can always regenerate this URL if we start getting spammed or something.
    webhook_url = 'https://hooks.slack.com/services/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'
    headers = {'Content-Type': 'application/json'}

    response = requests.post(webhook_url, json, headers)

    if response.status_code != 200:
        error_message = 'Push notification request sent to Slack returned an error. Status: {0}. Response: {1}'.format(response.status_code, response.text)

        raise ValueError(error_message)

