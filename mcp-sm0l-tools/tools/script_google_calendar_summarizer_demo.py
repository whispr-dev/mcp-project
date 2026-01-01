"""Google Calendar weekly summarizer demo.

Requires:
  GOOGLE_CRED_JSON  (service account JSON)

Prints a compact bullet summary of events in the next 7 days.
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
        print("Set GOOGLE_CRED_JSON to run.")
        return

    scopes = ["https://www.googleapis.com/auth/calendar.readonly"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(cred_path, scopes)
    svc = build("calendar", "v3", credentials=creds)

    now = datetime.now(timezone.utc)
    later = now + timedelta(days=7)

    items = svc.events().list(
        calendarId="primary",
        timeMin=now.isoformat(),
        timeMax=later.isoformat(),
        maxResults=50,
        singleEvents=True,
        orderBy="startTime",
    ).execute().get("items", [])

    def when(e):
        s = e.get("start", {}).get("dateTime") or e.get("start", {}).get("date")
        return s or "?"

    for e in items:
        print(f"- {when(e)} | {e.get('summary','(no title)')}")

    print("total", len(items))

if __name__ == "__main__":
    main()
