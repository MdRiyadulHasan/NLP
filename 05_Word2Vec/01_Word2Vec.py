from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize
import nltk

# Sample sentences
sentences = [
    "Word embeddings are a type of word representation that allows words to be represented as vectors in a continuous vector space.",
    "Word2Vec is a popular word embedding technique in natural language processing.",
    "It captures semantic relationships between words by mapping them to high-dimensional vectors.",
    "Similar words have similar vector representations in the Word2Vec model."
]

# Tokenize the sentences
tokenized_sentences = [word_tokenize(sentence.lower()) for sentence in sentences]

# Train Word2Vec model
model = Word2Vec(sentences=tokenized_sentences, vector_size=100, window=5, min_count=1, workers=4)

# Save the model (optional)
model.save("word2vec.model")

# Get vector representation of a word
vector_representation = model.wv['word']

# Find similar words
similar_words = model.wv.most_similar('word', topn=3)

# Print results
print("Vector representation of 'word':", vector_representation)
print("\nTop 3 similar words to 'word':", similar_words)
