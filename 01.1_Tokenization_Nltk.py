import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')  

# Sample text
text = "Tokenization is an important step in natural language processing."

# Tokenize the text
tokens = word_tokenize(text)

# Print the tokens
print(tokens)
