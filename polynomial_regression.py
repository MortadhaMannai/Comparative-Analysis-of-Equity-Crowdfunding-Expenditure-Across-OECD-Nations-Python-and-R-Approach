# Polynomial Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('crowdfunding_stats.csv', sep=',')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 13].values

# Fitting Linear Regression to the dataset
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y)

# Polynomial Regression dataset creation
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 3)
X_poly = poly_reg.fit_transform(X)
poly_reg.fit(X_poly, y)

# Fitting Polynomial Regression to the dataset
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)

# Visualising the Linear Regression results
plt.scatter(X, y, color = 'red')
plt.plot(X, lin_reg.predict(X), color = 'blue')
plt.title('Forecast vs. reality (Linear Regression)')
plt.xlabel('GDB')
plt.ylabel('Crowdfunding size')
plt.show()

# Visualising the Polynomial Regression results
plt.scatter(X, y, color = 'red')
plt.scatter(X, lin_reg_2.predict(poly_reg.fit_transform(X)), color = 'blue')
plt.title('Forecast vs. reality (Polynomial Regression)')
plt.xlabel('GDP')
plt.ylabel('Crowdfunding size')
plt.show()

# Visualising the Polynomial Regression results with linearity + smoother curve
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, lin_reg_2.predict(poly_reg.fit_transform(X_grid)), color = 'blue')
plt.title('Forecast vs. reality (Polynomial Regression)')
plt.xlabel('GDB')
plt.ylabel('Crowdfunding size')
plt.show()

# Predicting a new result with Linear Regression
lin_reg.predict(600000)

# Predicting a new result with Polynomial Regression
lin_reg_2.predict(poly_reg.fit_transform(600000))
