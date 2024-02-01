# import nltk
# from nltk.tokenize import word_tokenize
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

# # Sample text
# text = "The quick brown fox jumps over the lazy dog. Bangladesh is an independent country. We Love our country Very much. It's look beautifully in village."

# # Tokenize the text
# words = word_tokenize(text)

# # Perform POS tagging with NLTK
# pos_tags = nltk.pos_tag(words)

# # Display the word and its POS tag
# for word, pos_tag in pos_tags:
#     print(f"{word}: {pos_tag}")

import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Sample text
text = "The quick brown fox jumps over the lazy dog."

# Tokenize the text
words = word_tokenize(text)

# Perform POS tagging
pos_tags = pos_tag(words)

# Display the token and its POS tag
for token, pos_tag in pos_tags:
    print(f"{token}: {pos_tag}")
