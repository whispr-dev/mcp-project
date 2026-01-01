"""imbox minimal login skeleton.

Set IMAP_HOST, IMAP_USER, IMAP_PASS env vars to actually connect.
"""

import os

def main():
    try:
        from imbox import Imbox
    except Exception as e:
        print("Missing dependency or import failed:", e); return

    host = os.getenv("IMAP_HOST")
    user = os.getenv("IMAP_USER")
    pw = os.getenv("IMAP_PASS")
    if not (host and user and pw):
        print("Set IMAP_HOST/IMAP_USER/IMAP_PASS to connect.")
        return

    with Imbox(host, username=user, password=pw, ssl=True) as im:
        msgs = list(im.messages(limit=1))
        print("got", len(msgs), "message(s)")

if __name__ == "__main__":
    main()
