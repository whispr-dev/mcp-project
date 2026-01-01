from __future__ import annotations
import os

try:
    from openai import OpenAI
except ImportError:
    print("Missing dependency: openai. Install with: pip install openai")
    raise SystemExit(0)

if __name__ == "__main__":
    if not os.getenv("OPENAI_API_KEY"):
        print("Set OPENAI_API_KEY to run this demo.")
        raise SystemExit(0)
    client = OpenAI()
    # For new projects, the Responses API is the recommended entry point.
    r = client.responses.create(
        model="gpt-4o-mini",
        input="Say hello in one short sentence."
    )
    print(getattr(r, "output_text", None) or r)
