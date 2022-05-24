# -*- coding: utf-8 -*-
"""
Created on Mon May  9 22:37:03 2022

@author: Utilisateur
"""

import pandas as pd # data processing
from sklearn.linear_model import LinearRegression # OLS algorithm
import joblib

dfx = pd.read_csv("Xtrain.csv")
dfy = pd.read_csv("ytrain.csv")

dfxtrain = dfx.iloc[0:,1:]
dfytrain = dfy.iloc[0:,1:]

ols = LinearRegression()
ols.fit(dfxtrain,dfytrain)

joblib.dump(ols,'model.joblib')