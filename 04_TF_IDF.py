from sklearn.feature_extraction.text import TfidfVectorizer

# Sample documents
documents = [
    "I love natural language processing.",
    "NLP is fascinating and powerful.",
    "Python is a great programming language for NLP.",
]

# Create the TfidfVectorizer
vectorizer = TfidfVectorizer()

# Fit and transform the documents
X = vectorizer.fit_transform(documents)

# Get the feature names (words)
feature_names = vectorizer.get_feature_names_out()

# Get the TF-IDF representation as a dense matrix
tfidf_matrix = X.toarray()

# Print the feature names and the TF-IDF matrix
print("Feature Names:", feature_names)
print("TF-IDF Matrix:")
print(tfidf_matrix)
