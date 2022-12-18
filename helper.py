import streamlit as st
import pandas as pd
import numpy as np
import tensorflow as tf

from tensorflow.keras.preprocessing.sequence import pad_sequences

st.title('Uber pickups in NYC')