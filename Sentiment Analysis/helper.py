import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
import tensorflow_datasets as tfds
import pandas as pd


dataset = pd.read_csv('./sentiment.csv')
sentences = dataset['text'].tolist()
labels = dataset['sentiment'].tolist()
vocab_size = 1000
tokenizer = tfds.deprecated.text.SubwordTextEncoder.build_from_corpus(sentences, vocab_size, max_subword_length=5)

def predict_review(new_sentences, maxlen=100, show_padded_sequence=True):
  # Keep the original sentences so that we can keep using them later
  # Create an array to hold the encoded sequences
  model = load_model('./BLSTM_model1.h5')
  new_sequences = []
  max_length = 50
  # Convert the new reviews to sequences
  for i, frvw in enumerate(new_sentences):
    new_sequences.append(tokenizer.encode(frvw))

  trunc_type='post' 
  padding_type='post'

  # Pad all sequences for the new reviews
  new_reviews_padded = pad_sequences(new_sequences, maxlen=max_length, 
                                 padding=padding_type, truncating=trunc_type)             

  classes = model.predict(new_reviews_padded)

  # The closer the class is to 1, the more positive the review is
  return classes[0]