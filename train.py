import pandas as pd
import numpy as np
import re
import pickle
import nltk
from nltk.corpus import stopwords

from numpy import array
from keras.preprocessing.text import one_hot
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers.core import Activation, Dropout, Dense
from keras.layers import Flatten, LSTM, Bidirectional, Conv1D, GRU
from keras.layers import GlobalMaxPooling1D, GlobalAveragePooling1D
from keras.layers.embeddings import Embedding
from keras.preprocessing.text import Tokenizer

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer

# Loading dataset
dataset = pd.read_csv("dataset/text_emotion.csv")


# Pre-processing function
def preprocessing_text(sentence):

    # HTML Tags
    sentence = remove_tags(sentence)

    # Punctuation and numbers
    sentence = re.sub('[^a-zA-Z]', ' ', sentence)

    # Single character
    sentence = re.sub(r"\s+[a-zA-Z]\s+", ' ', sentence)

    # Multiple spaces
    sentence = re.sub(r'\s+', ' ', sentence)

    return sentence


TAG_RE = re.compile(r'<[^>]+>')


# Remove tags
def remove_tags(sentence):
    return TAG_RE.sub('', sentence)


# Pre-processed sentence
X = []
sentences = list(dataset['text'])
for sentence in sentences:
    X.append(preprocessing_text(sentence))


y = dataset['label']
# Binarize
encoder = LabelBinarizer()
y = encoder.fit_transform(y)


# Split train and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)


# Tokenize sentences to numbers
tokenizer = Tokenizer(num_words=10000)
tokenizer.fit_on_texts(X_train)

X_train = tokenizer.texts_to_sequences(X_train)
X_test = tokenizer.texts_to_sequences(X_test)

# Adding 1 because of reserved 0
vocab_size = len(tokenizer.word_index) + 1
