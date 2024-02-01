import spacy

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

# Sample text
text = "The quick brown fox jumps over the lazy dog. Bangladesh is an independent country"

# Process the text with spaCy
doc = nlp(text)

# Display the token and its POS tag
for token in doc:
    print(f"{token.text}: {token.pos_}")
