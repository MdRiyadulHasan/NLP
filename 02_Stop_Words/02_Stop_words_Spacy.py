import spacy

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

# Get spaCy's default stop words
stop_words_spacy = spacy.lang.en.stop_words.STOP_WORDS

print("spaCy Stop Words:")
print(stop_words_spacy)
