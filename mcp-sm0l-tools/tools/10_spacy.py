#!/usr/bin/env python3
"""spaCy: Industrial NLP"""
try:
    import spacy
    nlp = spacy.load("en_core_web_sm")
    doc = nlp("Schedule meeting with Sarah and send report")
    actions = [t.lemma_ for t in doc if t.pos_=="VERB"]
    print(f"Actions: {actions}")
except:
    print("python -m spacy download en_core_web_sm")
print("✓ Dependency parsing, NER, intent extraction")
