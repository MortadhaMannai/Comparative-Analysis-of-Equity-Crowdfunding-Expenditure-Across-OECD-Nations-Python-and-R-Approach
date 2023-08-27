# Multiple Linear Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Crowdfunding_stats.csv', sep=',')
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, 13].values

# Taking care of missing data (2nd to 8th column contain NaN values)
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(X[:, 2:9])
X[:, 2:9] = imputer.transform(X[:, 2:9])

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# no visual plotting - too many dimensions to show

# Predicting the Test set results
y_pred = regressor.predict(X_test)

# add a column of "1"
X = np.append(arr = np.ones((31,1)).astype(int), values = X, axis = 1)

# backward elimination
import statsmodels.formula.api as sm
X_opt = X[:, [0,1,2,3,4,5,6,7,8,9,10,11,12]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

X_opt = X[:, [0,4,6,8,9,10]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

X_opt = X[:, [0,4,6,8,10]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

X_opt = X[:, [0,6,8,10]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

