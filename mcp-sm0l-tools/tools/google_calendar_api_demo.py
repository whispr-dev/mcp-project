"""Google Calendar API minimal skeleton.

Requires service account JSON path in:
  GOOGLE_CRED_JSON

This demo only builds a client and lists next 1 event
if credentials are provided.
"""

import os
from datetime import datetime, timedelta, timezone

def main():
    try:
        from googleapiclient.discovery import build
        from oauth2client.service_account import ServiceAccountCredentials
    except Exception as e:
        print("Missing dependency or import failed:", e)
        return

    cred_path = os.getenv("GOOGLE_CRED_JSON")
    if not cred_path or not os.path.exists(cred_path):
        print("Set GOOGLE_CRED_JSON to a service account file to run.")
        return

    scopes = ["https://www.googleapis.com/auth/calendar.readonly"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(cred_path, scopes)
    svc = build("calendar", "v3", credentials=creds)

    now = datetime.now(timezone.utc).isoformat()
    later = (datetime.now(timezone.utc) + timedelta(days=7)).isoformat()

    events = svc.events().list(
        calendarId="primary",
        timeMin=now,
        timeMax=later,
        maxResults=1,
        singleEvents=True,
        orderBy="startTime",
    ).execute().get("items", [])

    print("events", len(events))
    if events:
        print(events[0].get("summary"))

if __name__ == "__main__":
    main()
