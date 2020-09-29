# Message_Emotion_Detector

## Project Description
The project aims to detect emotions in messages. 

## Key Concepts

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
