import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

# Download necessary resources
nltk.download('punkt')
nltk.download('stopwords')

# Sample text data
corpus = [
    'This is the first document.',
    'This document is the second document.',
    'And this is the third one.',
    'Is this the first document?'
]

# Tokenization
def tokenize(text):
    return word_tokenize(text)

# Remove stopwords
stop_words = set(stopwords.words('english'))

def remove_stopwords(tokens):
    return [word for word in tokens if word.lower() not in stop_words]

# Remove punctuation
def remove_punctuation(tokens):
    return [word for word in tokens if word not in string.punctuation]

# Preprocess the corpus
preprocessed_corpus = []
for text in corpus:
    tokens = tokenize(text)
    tokens = remove_stopwords(tokens)
    tokens = remove_punctuation(tokens)
    preprocessed_corpus.append(' '.join(tokens))

# TF-IDF Vectorization
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(preprocessed_corpus)

print("TF-IDF Matrix:")
print(X.toarray())
print("Feature Names:")
print(vectorizer.get_feature_names_out())
