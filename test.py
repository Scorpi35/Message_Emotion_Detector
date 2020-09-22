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

print("[INFO]: Preprocessing")
# Preprocess text
MAX_LENGTH = maxen = 100

def preprocessing_text(sen):

    # Removing html tags
    sentence = remove_tags(sen)

    # Remove punctuations and numbers
    sentence = re.sub('[^a-zA-Z]', ' ', sentence)

    # Single character removal
    sentence = re.sub(r"\s+[a-zA-Z]\s+", ' ', sentence)

    # Removing multiple spaces
    sentence = re.sub(r'\s+', ' ', sentence)

    return sentence


TAG_RE = re.compile(r'<[^>]+>')


def remove_tags(text):
    return TAG_RE.sub('', text)


# Tokenizer and pad sentence
sentence_processed = Tokenizer.texts_to_sequences(sentence)
sentence_processed = np.array(sentence_processed)
sentence_padded = tf.keras.preprocessing.sequence.pad_sequences(sentence_processed, padding='post', maxlen=MAX_LENGTH)

print("""[INFO]: Prediction\n\t{}""".format(sentence[0]))

