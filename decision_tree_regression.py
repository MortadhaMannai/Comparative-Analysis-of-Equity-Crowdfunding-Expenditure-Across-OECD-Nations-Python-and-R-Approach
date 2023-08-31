# Decision Tree Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('crowdfunding_stats.csv', sep=',')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 13].values

# Fitting Decision Tree Regression to the dataset
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state = 88)
regressor.fit(X, y)

# Predicting a new result
y_pred = regressor.predict(2500000)


# this one is non-continuous and ugly
plt.scatter(X, y, color = 'red')
plt.plot(X, regressor.predict(X), color = 'blue')
#plt.scatter(X, regressor.predict(X), color = 'blue')
plt.title('Forecast vs. reality (SVR)')
plt.xlabel('GDB')
plt.ylabel('Crowdfunding size')
plt.show()


# Visualising the Decision Tree Regression results (in ranges)
X_grid = np.arange(min(X), max(X), 100)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.title('Forecast vs. reality (Decision Tree Regression)')
plt.xlabel('GDB')
plt.ylabel('Crowdfunding size')
plt.show()

