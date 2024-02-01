from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import nltk

# Download the WordNet corpus (needed for lemmatization)
nltk.download('wordnet')
nltk.download('stopwords')

# Create a WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

# Sample text
text = """Natural Language Processing (NLP) is a fascinating field that combines linguistics and computer science to empower machines with language understanding. NLP algorithms parse and analyze human language, enabling applications like chatbots, sentiment analysis, and language translation.

Researchers and practitioners in NLP constantly strive to improve models' ability to handle diverse linguistic nuances, context, and ambiguities. Pre-trained language models, such as BERT and GPT, have revolutionized the field, achieving state-of-the-art results in various language-related tasks.

Despite advancements, challenges persist, including ethical considerations and biases in NLP models. Creating unbiased and inclusive language models remains a priority for the NLP community to ensure fair and equitable AI applications.

Continuous research and innovation drive the evolution of NLP, fostering improved communication between humans and machines. Nicely, Nicely, Nicely, Beautifully, additionally, warmly, locally, organizing, Caring.
"""

# Tokenize the text
words = word_tokenize(text)

# Create a set of English stopwords
stop_words = set(stopwords.words('english'))
words = [word for word in words if word.lower() not in stop_words]
# Lemmatize the words, excluding stopwords
lemmatized_words = [lemmatizer.lemmatize(word) for word in words if word.lower() not in stop_words]

# Print the original words and their lemmas
for original, lemma in zip(words, lemmatized_words):
    print(f"{original} -> {lemma}")
