import numpy as np
import tensorflow
import pickle
import re

# Input sentence
sentence = ["Do not ever come back to me, understood?"]

# Loading class
classNames = np.load("./data/class_names.npy")