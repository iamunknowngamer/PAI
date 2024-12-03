import nltk
nltk.download('punkt')

#tokenization
from nltk.tokenize import word_tokenize, sent_tokenize

text = "This is a sample sentence. Tokenize me, please."

words = word_tokenize(text)
print("Word Tokenization:")
print(words)

sentences = sent_tokenize(text)
print("Sentence Tokenization:")
print(sentences)

#stemming
# import nltk
# from nltk.stem import PorterStemmer

# words = {"jumping", "jumps", "jumped", "running", "runner", "easily"}

# stemmer = PorterStemmer()
# stemmed_words = [stemmer.stem(word) for word in words]

# print("Original Words: ", words)
# print("Stemmed Words: ", stemmed_words)


#lemetization
# import nltk
# from nltk.stem import WordNetLemmatizer
# from nltk.corpus import wordnet

# words = {"jumping", "jumps", "jumped", "running", "runner", "easily"}

# lemetizar = WordNetLemmatizer()

# lemetized_words_n = [lemetizar.lemmatize(word) for word in words]
# lemetized_words_v = [lemetizar.lemmatize(word, pos='v') for word in words]

# print("Original Words: ", words)
# print("Stemmed Words as noun: ", lemetized_words_n)
# print("Stemmed Words as verb: ", lemetized_words_v)


#stopwords
# import nltk
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize

# nltk.download('stopwords')
# nltk.download('punkt')

# text = "This is a sample sentence with some stopwords that we want to remove."

# words = word_tokenize(text)

# stop_words = set(stopwords.words('english'))

# filtered_words = [word for word in words if word.lower() not in stop_words]

# print("Original Words: ", words)
# print("Stemmed Words as noun: ", filtered_words)


# #stemming a paragraph
# import nltk
# from nltk.corpus import stopwords
# from nltk.stem import PorterStemmer

# text = "The running dogs were running fast through the park. They had run for hours, and they were exhausted but still running energetically. The runners in the race were also feeling the same way, as the race had been challenging."

# sentences = nltk.sent_tokenize(text)
# stemmer = PorterStemmer()

# for i in range(len(sentences)):
#     words = nltk.tokenize(sentences[i])
#     words = [stemmer.stem(word) for word in words if word not in set(stopwords.words('english'))]
#     sentences[i] = ' '.join(words)

# print(sentences)
