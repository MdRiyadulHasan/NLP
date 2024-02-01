import spacy

# Load the spaCy English NER model
val = spacy.load("en_core_web_sm")

# Process a text
text = "Apple Inc. is a technology company based in Cupertino, California."
doc = val(text)

# Extract named entities
for ent in doc.ents:
    print(f"{ent.text}: {ent.label_}")