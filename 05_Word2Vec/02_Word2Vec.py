from nltk.tokenize import word_tokenize
from nltk.corpus import reuters
from gensim.models import Word2Vec
import nltk 
# Load NLTK's Reuters corpus
nltk.download('reuters')
corpus = reuters.sents()

# Tokenize the sentences
tokenized_corpus = [sentence for sentence in corpus]
print("Hello", tokenized_corpus)
print("\n")

# Train Word2Vec model using Gensim
nltk_model = Word2Vec(sentences=tokenized_corpus, vector_size=100, window=5, min_count=1, workers=4)

# Save the model (optional)
nltk_model.save("nltk_word2vec.model")

# Get vector representation of a word
vector_representation = nltk_model.wv['word']

# Find similar words
similar_words = nltk_model.wv.most_similar('word', topn=3)

# Print results
print("NLTK Word2Vec:")
print("Vector representation of 'word':", vector_representation)
print("Top 3 similar words to 'word':", similar_words)
