from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Create a PorterStemmer
stemmer = PorterStemmer()

# Sample text
text = """Natural Language Processing (NLP) is a fascinating field that combines linguistics and computer science to empower machines with language understanding. NLP algorithms parse and analyze human language, enabling applications like chatbots, sentiment analysis, and language translation.Researchers and practitioners in NLP constantly strive to improve models' ability to handle diverse linguistic nuances, context, and ambiguities. Pre-trained language models, such as BERT and GPT, have revolutionized the field, achieving state-of-the-art results in various language-related tasks.Despite advancements, challenges persist, including ethical considerations and biases in NLP models. Creating unbiased and inclusive language models remains a priority for the NLP community to ensure fair and equitable AI applications.Continuous research and innovation drive the evolution of NLP, fostering improved communication between humans and machines. Nicely, Beautifully, additionally, warmly, locally, organizing. cries, crys, cried.
"""

# Tokenize the text
words = word_tokenize(text)

# Stem the words
stemmed_words = [stemmer.stem(word) for word in words]

# Print the original words and their stems
for original, stemmed in zip(words, stemmed_words):
    print(f"{original} -> {stemmed}")
