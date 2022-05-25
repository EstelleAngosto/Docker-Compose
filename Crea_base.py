# -*- coding: utf-8 -*-
"""
Created on Mon May  9 21:13:48 2022

@author: Utilisateur
"""

# import pandas as pd # data processing
# from sklearn.model_selection import train_test_split # data split

# df = pd.read_csv("House_Data.csv")
# df = df.dropna()
# df.MasVnrArea = df.MasVnrArea.astype(int)

# columns = ['LotArea','MasVnrArea','BsmtUnfSF','TotalBsmtSF','1stFlrSF','2ndFlrSF','GrLivArea','GarageArea','WoodDeckSF','OpenPorchSF']

# X_var = df[columns].values
# Y_var = df['SalePrice'].values
# X_train, X_test, y_train, y_test = train_test_split(X_var,Y_var,test_size=0.20, random_state=0)

import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split

data = fetch_california_housing() #Chargement des données.
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target)

pd.DataFrame(X_train).to_csv("Xtrain.csv")
pd.DataFrame(y_train).to_csv("ytrain.csv")
pd.DataFrame(X_test).to_csv("Xtest.csv")
pd.DataFrame(y_test).to_csv("ytest.csv")