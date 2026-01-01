"""Slack thread summarizer skeleton.

Requires:
  SLACK_BOT_TOKEN

This demo does not call Slack.
It prints the minimal request shape.
"""

import os, json

def main():
    token = os.getenv("SLACK_BOT_TOKEN")
    if not token:
        print("Set SLACK_BOT_TOKEN to enable requests.")
        return

    payload = {"channel": "C123", "ts": "123.456"}
    print("POST https://slack.com/api/conversations.replies")
    print("headers: Authorization: Bearer $SLACK_BOT_TOKEN")
    print("json:", json.dumps(payload))

if __name__ == "__main__":
    main()
