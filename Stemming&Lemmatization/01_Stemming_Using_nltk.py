from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Create a PorterStemmer
stemmer = PorterStemmer()

# Sample text
text = "Stemming is an important step in natural language processing."

# Tokenize the text
words = word_tokenize(text)

# Stem the words
stemmed_words = [stemmer.stem(word) for word in words]

# Print the original words and their stems
for original, stemmed in zip(words, stemmed_words):
    print(f"{original} -> {stemmed}")
