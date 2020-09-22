import numpy as np
import tensorflow
import pickle
import re

# Input sentence
sentence = ["Do not ever come back to me, understood?"]

# Loading Emotion types and classes
classNames = np.load("./data/class_names.npy")

print("[INFO]: Loading Tokens")
with open('./data/tokenizer.pickle', 'rb') as handle:
        Tokenizer = pickle.load(handle)

print(Tokenizer.texts_to_sequences(sentence))