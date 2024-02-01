import spacy

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

# Process a text
text = "I love natural language processing!"
doc = nlp(text)

# Access tokens and their attributes
for token in doc:
    print(f"Token: {token.text}, Start: {token.idx}, End: {token.idx + len(token)}")
