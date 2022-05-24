# -*- coding: utf-8 -*-
"""
Created on Mon May  9 22:37:04 2022

@author: Utilisateur
"""

import pandas as pd # data processing
import matplotlib.pyplot as plt # visualization
from sklearn.metrics import explained_variance_score as evs # evaluation metric
from sklearn.metrics import r2_score as r2 # evaluation metric
import joblib
from termcolor import colored as cl # text customization


dfx = pd.read_csv("Xtest.csv")
dfy = pd.read_csv("ytest.csv")

dfxtest = dfx.iloc[0:,1:]
dfytest = dfy.iloc[0:,1:]

ols = joblib.load('model.joblib')
ols_yhat = ols.predict(dfxtest)

plt.figure(figsize=(10, 6))
plt.scatter(ols_yhat, dfytest)
plt.xlabel('True price')
plt.ylabel('Predicted price')
plt.title('Linear Regression')
plt.tight_layout()

print(cl('Explained Variance Score of OLS model is {}'.format(evs(dfytest, ols_yhat)), attrs = ['bold']))
print(cl('R-Squared of OLS model is {}'.format(r2(dfytest, ols_yhat)), attrs = ['bold']))
