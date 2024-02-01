import spacy

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

# Sample text
text = "Stemming is an important step in natural language processing."

# Process the text with spaCy
doc = nlp(text)

# Get the stems using lemmatization (as spaCy does not have a dedicated stemmer)
stems = [token.lemma_ for token in doc]

# Print the original words and their stems
for original, stem in zip(doc, stems):
    print(f"{original.text} -> {stem}")
