import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import math
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers import LSTM
import preprocessing

# FOR REPRODUCIBILITY
np.random.seed(7)

# Importing Dataset
dataset = pd.read_csv('apple_share_price.csv')
print(dataset)