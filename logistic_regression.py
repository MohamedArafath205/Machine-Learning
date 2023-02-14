# -*- coding: utf-8 -*-
"""Logistic Regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16LdjaIuQcoPYdznLCStD9GSzpz-joFFT
"""

# 1. take the dataset and create dataframes
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/ameenmanna8824/DATASETS/main/IRIS.csv')
df

# 4. splitting into train and test
x = df.iloc[:,0:4].values
y = df.iloc[:,4].values

print(x)
print(y)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,random_state=0)

# 7. apply classifier, regressor or clusterer
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

# 8. fitting the model
model.fit(x_train, y_train)

# 9. Predict the output
y_pred = model.predict(x_test)
y_pred

# 10. Accuracy
from sklearn.metrics import accuracy_score
accuracy_score(y_pred, y_test)*100

