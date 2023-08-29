# SVR

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Import the dataset
dataset = pd.read_csv('crowdfunding_stats.csv', sep=',')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 13].values

# Taking care of missing data (2nd to 8th column contain NaN values)
#from sklearn.preprocessing import Imputer
#imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
#imputer = imputer.fit(X[:, 2:9])
#X[:, 2:9] = imputer.transform(X[:, 2:9])

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X)
y = sc_y.fit_transform(y)

# Fitting SVR to the dataset
from sklearn.svm import SVR
regressor = SVR(kernel = 'rbf')
regressor.fit(X, y)

# Predicting a new result
# version with 11 variables
#y_pred = regressor.predict(sc_X.transform(np.array([[600000, 4, 56, 43, 2, 4, 21, 43, 84, 2, 22]])))
# version with one variable (GDP)
y_pred = regressor.predict(sc_X.transform(np.array([[600000]])))
y_pred = sc_y.inverse_transform(y_pred)

# Visualising the SVR results - United Kingdom has been automatically treated as an outlier
plt.scatter(X, y, color = 'red')
#plt.plot(X, regressor.predict(X), color = 'blue')
plt.scatter(X, regressor.predict(X), color = 'blue')
plt.title('Forecast vs. reality (SVR)')
plt.xlabel('GDB')
plt.ylabel('Crowdfunding size')
plt.show()

# Visualising the SVR results (for higher resolution and smoother curve)
X_grid = np.arange(min(X), max(X), 0.01) # choice of 0.01 instead of 0.1 step because the data is feature scaled
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.title('Forecast vs. reality (SVR)')
plt.xlabel('GDB')
plt.ylabel('Crowdfunding size')
plt.show()