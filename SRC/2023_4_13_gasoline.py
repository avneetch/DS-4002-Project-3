# -*- coding: utf-8 -*-
"""2023.4.13.Gasoline.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18gIcsgival-xdYqrEbyfWwVbWdDHPO7K
"""

# import libraries
import pandas as pd

# import data
from google.colab import files
uploaded = files.upload()

import io
gas_raw = pd.read_csv('Gas_Price_Central_Atlantic.csv')
# Dataset is now stored in a Pandas Dataframe

gas_raw

"""gas = gas_raw.drop(gas_raw.columns[2:], axis=1)
gas
"""

gas = gas_raw.drop(gas_raw.columns[2:], axis=1)
gas

import matplotlib.pyplot as plt
# plt.plot(x=gas['Date'], y=gas['Price'], linestyle = 'dotted')
gas.plot.line()

import pandas as pd
from datetime import datetime
def parse(x):return pd.datetime.strptime(x, "%b %d, %Y")
df = pd.read_csv('Gas_Price_Central_Atlantic.csv', index_col=0, date_parser=parse)
df = df.drop(gas_raw.columns[2:], axis=1)
df

df.isnull().sum()

df.describe()

df.info()

train_data = df['1993-04-05':'2016-12-31']
test_data = df['2017-01-01':]
print("Observations: %d" % (len(df)))
print("Train dataset:" ,train_data.shape)
print("Test dataset:" ,test_data.shape)

ax = train_data.plot(figsize=(10,5))
test_data.plot(ax=ax, color='r')
plt.legend(['train','test'])

# Data normalization (scale down and normalize)
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range = (0,1))
train_data_scaled = scaler.fit_transform(train_data)
print(train_data_scaled); print(train_data_scaled.shape)

# Create a data structure with 60 time lags and 1 output
import numpy as np
X_train = []
y_train = []
for i in range(60, len(train_data_scaled)):
    X_train.append(train_data_scaled[i-60:i,0])
    y_train.append(train_data_scaled[i,0])
X_train, y_train = np.array(X_train), np.array(y_train)
print(X_train); print(); print(y_train)

# Reshape data
X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
print(X_train.shape); print(); print(X_train)

# Recurrent neural network
import tensorflow as tf
import keras
from keras.callbacks import ModelCheckpoint, EarlyStopping

model = tf.keras.Sequential()
# adding 1st LSTM layer and some dropout regularization
model.add(tf.keras.layers.LSTM(units=50, input_shape=(X_train.shape[1], 1), return_sequences=True, activation = 'relu'))
model.add(tf.keras.layers.Dropout(0.2))
# adding 2nd LSTM layer and some dropout regularization
model.add(tf.keras.layers.LSTM(units=50, return_sequences=True))
model.add(tf.keras.layers.Dropout(0.2))
# adding 3rd LSTM layer and some dropout regularization
model.add(tf.keras.layers.LSTM(units=50, return_sequences=True))
model.add(tf.keras.layers.Dropout(0.2))
# adding 4th LSTM layer and some dropout regularization
model.add(tf.keras.layers.LSTM(units=50))
model.add(tf.keras.layers.Dropout(0.2))
# adding output layer
model.add(tf.keras.layers.Dense(units=1))
#compiling RNN
model.compile(loss='mean_squared_error', optimizer='adam')
early_stopping = EarlyStopping(monitor='loss', patience=10)
# fitting RNN on training set
model.fit(X_train, y_train, epochs= 50, batch_size=32, 
          verbose=2, callbacks=[early_stopping])

# Append previous 60 records from training set to test set

dataset_total = pd.concat((train_data, test_data), axis=0)
print(dataset_total)
dataset_total = pd.concat((train_data, test_data), axis=0)
inputs = dataset_total[len(dataset_total) - len(test_data)- 60:].values
inputs = inputs.reshape(-1,1)
inputs = scaler.transform(inputs) # transforming input data
X_test = []
y_test = []
for i in range (60, 387):
    X_test.append(inputs[i-60:i, 0])
    y_test.append(train_data_scaled[i,0])

      
X_test, y_test = np.array(X_test), np.array(y_test)
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
pred_price = model.predict(X_test)
pred_price = scaler.inverse_transform(pred_price)
print(pred_price)

a = pd.DataFrame(pred_price)
a.rename(columns = {0: 'Predicted'}, inplace=True);
a.index = test_data.index
compare = pd.concat([test_data, a],1)
compare

plt.figure(figsize= (15,5))
plt.plot(compare['Price'], color= 'red', label= 'Actual Gas Price')
plt.plot(compare['Predicted'], color= 'blue', label= 'Predicted Price')
plt.title("Gas Price Prediction for Central Atlantic Region")
plt.xlabel('Time')
plt.ylabel('Gas Price')
plt.legend(loc='best')
plt.show()

from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import math

test_score = math.sqrt(mean_squared_error(compare['Price'], compare.Predicted))
print('Test Score: %.2f RMSE' % (test_score))
# Explanied variance score: 1 is perfect prediction
print('Variance score (test): %.2f' % r2_score(test_data, pred_price))











