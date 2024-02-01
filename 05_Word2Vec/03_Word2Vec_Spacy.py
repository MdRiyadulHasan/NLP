import spacy
from gensim.models import Word2Vec

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Sample text
text = """Natural Language Processing (NLP) is a fascinating word that combines linguistics and computer science to empower machines with language understanding."""

# Process the text with spaCy
doc = nlp(text)

# Extract tokenized sentences
tokenized_sentences = [[token.text.lower() for token in sent] for sent in doc.sents]

# Train Word2Vec model using Gensim
spacy_model = Word2Vec(sentences=tokenized_sentences, vector_size=100, window=5, min_count=1, workers=4)

# Save the model (optional)
spacy_model.save("spacy_word2vec.model")

# Get vector representation of a word
vector_representation = spacy_model.wv['word']

# Find similar words
similar_words = spacy_model.wv.most_similar('word', topn=3)

# Print results
print("\nspaCy Word2Vec:")
print("Vector representation of 'word':", vector_representation)
print("Top 3 similar words to 'word':", similar_words)
