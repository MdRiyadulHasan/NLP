from sklearn.feature_extraction.text import CountVectorizer

# Sample documents
documents = [
    "I love natural language processing. I love natural language",
    "NLP is fascinating and powerful.",
    "Python is a great programming language for NLP.",
]

# Create the CountVectorizer
vectorizer = CountVectorizer()

# Fit and transform the documents
X = vectorizer.fit_transform(documents)

# Get the feature names (words)
feature_names = vectorizer.get_feature_names_out()

# Get the Bag of Words representation as a dense matrix
bow_matrix = X.toarray()

# Print the feature names and the Bag of Words matrix
print("Feature Names:", feature_names)
print("Bag of Words Matrix:")
print(bow_matrix)
