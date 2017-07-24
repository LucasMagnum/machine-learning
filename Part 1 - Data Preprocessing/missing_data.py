# Data Preprocessing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import Imputer

# Importing the dataset
dataset = pd.read_csv('Data.csv')

# Get all columns excluding the last
X = dataset.iloc[:, :-1].values

# Get the last column
y = dataset.iloc[:, 3].values

# Prepare imputer to replace missing values
imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)
imputer = imputer.fit(X[:, 1:3])

# Replace missing data with new data
X[:, 1:3] = imputer.transform(X[:, 1:3])
