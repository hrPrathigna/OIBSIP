# -*- coding: utf-8 -*-
"""email.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12Rs0o90sxgDfW1BZZRuxTVcvkvrt5HPh

**Email Spam Detection With Machine Learning**
Spam mail, or junk mail, is a type of email
that is sent to a massive number of users at one time, frequently containing cryptic messages, scams, or most dangerously, phishing content.
In this Project,we use Python to build an email spam detector.Then, use machine learning to
train the spam detector to recognize and classify emails into spam and non-spam.
"""

#Import Library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Import Data
mail = pd.read_csv('spam.csv',encoding='latin')

mail.head()

print(mail)

#Describe Data
mail.info()

mail.describe()

mail.shape

#Data Preprocessing
mail.isnull().sum()

mail.columns

mail.drop(columns=['Unnamed: 2','Unnamed: 3','Unnamed: 4'],inplace=True)

mail.shape

mail.head()

spam=mail.rename(columns={'v1':'spam','v2':'Message'})

spam.shape

spam.duplicated().sum()

spam.drop_duplicates(keep='first',inplace=True)

spam.shape

from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
spam['spam'] = encoder.fit_transform(spam['spam'])
spam['spam']

#Data Visualization
plt.pie(spam['spam'].value_counts(),labels=['ham','spam'],autopct="%0.2f")
plt.show()

#Define Target Variable (y) and Feature Variables (X)
y=spam['spam']
X=spam['Message']

print(y)

print(X)

#Train Test Split
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=5)

X_train.shape, X_test.shape, y_train.shape, y_test.shape

#Modeling
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import svm

cv=CountVectorizer()

X_train_cv=cv.fit_transform(X_train)
X_test_cv=cv.transform(X_test)

print(X_train_cv)

from sklearn.linear_model import LogisticRegression
model=LogisticRegression()

model.fit(X_train_cv,y_train)
prediction_train=model.predict(X_train_cv)

model.intercept_

model.coef_

#predict model
y_pred = model.predict(X_test_cv)

y_pred

#model accuracy
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error, mean_squared_error
from sklearn.metrics import accuracy_score

mean_absolute_error(y_test,y_pred)

mean_absolute_percentage_error(y_test,y_pred)

print(accuracy_score(y_train,prediction_train)*100)

prediction_test=model.predict(X_test_cv)

print(accuracy_score(y_test,prediction_test)*100)