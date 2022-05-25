# -*- coding: utf-8 -*-
"""
Created on Tue May 10 22:35:46 2022

@author: Utilisateur
"""
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split

data = fetch_california_housing() #Chargement des données.
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target)

pd.DataFrame(X_train).to_csv("B_Xtrain.csv")
pd.DataFrame(y_train).to_csv("B_ytrain.csv")
pd.DataFrame(X_test).to_csv("B_Xtest.csv")
pd.DataFrame(y_test).to_csv("B_ytest.csv")
