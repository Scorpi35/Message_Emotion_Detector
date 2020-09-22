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

print("[INFO]: Loading Model")
model = tf.keras.models.load_model("./data/model_final.model")


