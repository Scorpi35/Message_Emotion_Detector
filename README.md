# Emotion detection from Messages

## Project Description
**Sentiment Analysis** tends to evaluate 3 basic emotions:- **Positive, Neutral & Negative.** I tended to take things little farther and classify the text respective to 7 emotions:- **Anger, Disgust, Fear, Gult, Joy, Sadness and Shame**. This repository contains the dataset for training a model, basic sequential training procedure and testing of the model. The model has been illutratively implemented in a website where emotios behind messages are detected.

## Website
http://emotion-detection-messenger.herokuapp.com/

## Key Concepts
* Sentiment Analysis
* Emotion Detection

## Dataset
* **Name:-** ISEAR Dataset(https://www.kaggle.com/shrivastava/isears-dataset)
* **Rows:-** 7516
* **Columns:-** label, text
* **Types of emotions(label):-** Anger, Disgust, Fear, Guilt, Joy, Sadness, Shame

## Tools and libraries
* **Language:-** Python
* **IDE:-** PyCharm
* **Libraries:-** nltk, numpy, tensorflow, numpy, keras, sklearn, pandas

## Algorithm
1. Pre-processing
2. Tokenization
3. Generate word embeddings
4. Training LSTM Model with bidirectional layers

## Training Description
#### LSTM 
* **Model:-** Sequential, 1 Embbedding layer, 3 Bidirectional layers, 2 Dense layers
* **Optimizer:-** Adam
* **Epochs:-** 150
* **Batch Size:-** 128
* **Validation Split:-** 0.2

## Future Extension
* Integration of Plutchik's Wheel of Emotions
* Analyzing context of conversation
* Introducing time feature
