import nltk
nltk.download('punkt')
nltk.download('stopwords')
from gensim.models import Word2Vec
from nltk.corpus import stopwords
import re

# Input paragraph
paragraph = """Spurred by the Pakistan Movement, which sought a homeland for the Muslims of British India,
and election victories in 1946 by the All-India Muslim League, Pakistan gained independence in 1947 after the Partition of the
British Indian Empire, which awarded separate statehood to its Muslim-majority regions and was accompanied by an unparalleled mass migration and loss of life."""

# Preprocessing the data
text = re.sub(r'\[[0-9]*\]', ' ', paragraph)
text = re.sub(r'\s+', ' ', text)
text = re.sub(r'[^a-zA-Z]', ' ', text)
text = re.sub(r'\s+', ' ', text)

# Preparing the dataset
sentences = nltk.sent_tokenize(text)
sentences = [nltk.word_tokenize(sentence) for sentence in sentences]

for i in range(len(sentences)):
    sentences[i] = [word for word in sentences[i] if word not in stopwords.words('english')]

# Training the Word2Vec model
model = Word2Vec(sentences, min_count=1)

# Words in the vocabulary
words = model.wv.vocab

# Finding word vectors
vector = model.wv['muslims']

# Most similar words
similar = model.wv.most_similar('pakistan')

print("Words in Vocabulary:", words)
print("Vector for 'muslims':", vector)
print("Words most similar to 'pakistan':", similar)
