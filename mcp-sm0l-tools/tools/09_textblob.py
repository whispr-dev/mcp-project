#!/usr/bin/env python3
"""TextBlob: Quick NLP"""
try:
    from textblob import TextBlob
    t = TextBlob("I love Python automation!")
    print(f"Sentiment: {t.sentiment}")
    print(f"Noun phrases: {t.noun_phrases}")
except:
    print("pip install textblob")
print("✓ Sentiment, translation, spell check")
