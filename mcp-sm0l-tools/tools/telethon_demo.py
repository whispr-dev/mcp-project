"""telethon minimal client construction.

Requires you to set TELETHON_API_ID and TELETHON_API_HASH env vars
for real use. This demo won't connect.
"""

import os

def main():
    try:
        from telethon import TelegramClient
    except Exception as e:
        print("Missing dependency or import failed:", e); return

    api_id = os.getenv("TELETHON_API_ID")
    api_hash = os.getenv("TELETHON_API_HASH")
    if not (api_id and api_hash):
        print("Set TELETHON_API_ID and TELETHON_API_HASH to connect.")
        return

    client = TelegramClient("sm0l_session", int(api_id), api_hash)
    print("client ready:", type(client).__name__)

if __name__ == "__main__":
    main()
