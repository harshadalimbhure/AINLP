# Assignment No. 01

# Import library
import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")

# Define input text
about_text = "India is my country. Maharashtra is my state."

# 1. Tokenization
about_doc = nlp(about_text)
print("1. Tokenization:")
for token in about_doc:
    print(token, token.idx)

# 2. Stop Words Removal
print("\n2. Stop Words Removal:")
print([token for token in about_doc if not token.is_stop])

# 3. Lemmatization
print("\n3. Lemmatization:")
for token in about_doc:
    if token.text != token.lemma_:
        print(f"{token.text:>15} : {token.lemma_}")

# 4. Part of Speech Tagging
print("\n4. Part of Speech Tagging:")
for token in about_doc:
    print(f"""
TOKEN: {token.text}
=====
TAG: {token.tag_:10} POS: {token.pos_}
EXPLANATION: {spacy.explain(token.tag_)}
""")
