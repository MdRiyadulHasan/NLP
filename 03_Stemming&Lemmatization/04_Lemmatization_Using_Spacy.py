import spacy
from spacy.lang.en.stop_words import STOP_WORDS

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

# Sample text
text = """Natural Language Processing (NLP) is a fascinating field that combines linguistics and computer science to empower machines with language understanding. NLP algorithms parse and analyze human language, enabling applications like chatbots, sentiment analysis, and language translation.Researchers and practitioners in NLP constantly strive to improve models' ability to handle diverse linguistic nuances, context, and ambiguities. Pre-trained language models, such as BERT and GPT, have revolutionized the field, achieving state-of-the-art results in various language-related tasks.Despite advancements, challenges persist, including ethical considerations and biases in NLP models. Creating unbiased and inclusive language models remains a priority for the NLP community to ensure fair and equitable AI applications.Continuous research and innovation drive the evolution of NLP, fostering improved communication between humans and machines. Nicely, Beautifully, additionally, warmly, locally, organizing. cries, crys, cried.
"""

# Process the text with spaCy
doc = nlp(text)
words = [token.text for token in doc if token.text.lower() not in STOP_WORDS]
print("hjkl", words)
# Get the lemmas excluding stopwords
lemmas = [token.lemma_ for token in doc if token.lower_ not in STOP_WORDS]

# Print the original words and their lemmas
for original, lemma in zip(words, lemmas):
    print(f"{original} -> {lemma}")
