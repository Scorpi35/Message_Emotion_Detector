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

    sentence = remove_tags(sentence)
    # Remove punctuations and numbers

    sentence = re.sub('[^a-zA-Z]', ' ', sentence)

    # Single character removal
    sentence = re.sub(r"\s+[a-zA-Z]\s+", ' ', sentence)

    # Removing multiple spaces
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
    print(preprocessing_text(sentence))


