import spacy

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

# Sample text
text = "Tokenization is an important step in natural language processing."

# Process the text with spaCy
doc = nlp(text)

# Get the tokens
tokens = [token.text for token in doc]

# Print the tokens
print(tokens)
