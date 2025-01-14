# -*- coding: utf-8 -*-
"""Faruq - Loan DataSet Assignment.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Z__er7n4JDchhuLvXe9vryj9F0kGw_59
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#df = pd.read_csv('/content/drive/MyDrive/loan_approval_dataset.csv')
df = pd.read_csv('./loan_approval_dataset.csv')
df.head()

# prompt: Using dataframe df: display column education

df[' education'].value_counts()

from sklearn import preprocessing
label = preprocessing.LabelEncoder()

df[' education'] = label.fit_transform(df[' education'] )
print(df[' education'].unique())
df[' education']
df.head()

df[' self_employed'] = label.fit_transform(df[' self_employed'] )
print(df[' self_employed'].unique())
df[' self_employed']

df[' loan_status'] = label.fit_transform(df[' loan_status'] )
print(df[' loan_status'].unique())
df[' loan_status']

df.describe()

#df.info()
df.head()

y = df[' loan_status']
X = df.drop(" loan_status",axis=1)

y.head()
X.head()

from sklearn.linear_model import LogisticRegression

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# instantiate the model (using the default parameters)
logreg = LogisticRegression(random_state=16)

# fit the model with data
logreg.fit(X_train, y_train)

y_pred = logreg.predict(X_test)
# Evaluate model performance
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")