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

max_len = 100

# Pad sequences to max length with post padding.
X_train = pad_sequences(X_train, padding='post', maxlen=max_len)
X_test = pad_sequences(X_test, padding='post', maxlen=max_len)

# Load embedding file
embeddings_dictionary = dict()
with open('../glove.6B.100d.txt', encoding="utf8") as glove_file:
    for line in glove_file:
        records = line.split()
        word = records[0]
        vector_dimensions = np.asarray(records[1:], dtype='float32')
        embeddings_dictionary [word] = vector_dimensions


embedding_matrix = np.zeros((vocab_size, 100))

for word, index in tokenizer.word_index.items():
    embedding_vector = embeddings_dictionary.get(word)
    if embedding_vector is not None:
        embedding_matrix[index] = embedding_vector
print("INFO:- Creating Model")

# LSTM Model with bidirectional layer
model = Sequential([
    Embedding(vocab_size, 100, weights=[embedding_matrix], input_length=max_len, trainable=False),
    Bidirectional(LSTM(50, dropout=0.2, recurrent_dropout=0.2, return_sequences=True)),
    Bidirectional(LSTM(54, dropout=0.3, recurrent_dropout=0.3, return_sequences=True)),
    Bidirectional(LSTM(60, dropout=0.3, recurrent_dropout=0.3)),
    Dense(64, activation="relu"),
    Dense(7, activation="softmax")
])


# # compile model
# model.compile(optimizer="adam", loss='categorical_crossentropy', mectrics=['accuracy'])
# print("INFO: Starting Training")



# # Train model
# history = model.fit(X_train, y_train, batch_size=128, epochs=1, verbose=1, validation_split=0.2)
#
# # Save model, classes and tokenizer file
# model.save("model_final.model")


