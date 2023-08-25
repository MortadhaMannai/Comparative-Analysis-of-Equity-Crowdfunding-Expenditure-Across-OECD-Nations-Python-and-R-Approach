# Simple Linear Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Dataset import
# use dot-separated numbers in cells for easier translation to float format
dataset = pd.read_csv('Crowdfunding_stats.csv', sep=',')
X = dataset.iloc[:, 1:2].values  # one column at a time, GDP column here
y = dataset.iloc[:, 13].value

# if there is any NaN value - convert to 0
X[np.isnan(X)] = 0

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

# Simple Linear Regression - Fit to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Prediction of the Test set results
y_pred = regressor.predict(X_test)

# Visualisation of the Training set results
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('GDP vs Crowdfunding in OECD (Training set)')
plt.xlabel('GDP')
plt.ylabel('Crowdfunding size')
plt.show()

# Visualisation of the Test set results
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('GDP vs Crowdfunding in OECD (Test set)')
plt.xlabel('GDP')
plt.ylabel('Crowdfunding size')
plt.show()