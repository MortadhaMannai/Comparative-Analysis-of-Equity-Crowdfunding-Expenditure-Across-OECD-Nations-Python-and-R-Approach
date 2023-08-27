# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset - impact of price and number of accommodations
dataset = pd.read_csv('airbnb_warsaw_without_outliers.csv',sep=';')
X = dataset.iloc[:, [7, 9]].values
y = dataset.iloc[:, 4].values

def PrepareForPrediction(X, y):
    global X_train, X_test, y_train, y_test
    from sklearn.cross_validation import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)
    return X_train, X_test, y_train, y_test
    
    
# Splitting the dataset into the Training set and Test set & Feature Scaling
PrepareForPrediction(X, y)

# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

def visualizeResults(X_set, y_set):
    from matplotlib.colors import ListedColormap
    X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                         np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
    plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
                 alpha = 0.75, cmap = ListedColormap(('red', 'green')))
    plt.xlim(X1.min(), X1.max())
    plt.ylim(X2.min(), X2.max())
    for i, j in enumerate(np.unique(y_set)):
        plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                    c = ListedColormap(('red', 'green'))(i), label = j)
    plt.title('Logistic Regression')
    plt.xlabel('number of bedrooms')
    plt.ylabel('price in PLN')
    plt.legend()
    plt.show()

# Visualising the Training set results
visualizeResults(X_train, y_train)


# Visualising the Test set results
visualizeResults(X_test, y_test)

# good prediction ratio = 0.59422

_____

# changing the dataset - impact of price and number of bedrooms
dataset = pd.read_csv('airbnb_warsaw_without_outliers.csv',sep=';')
X = dataset.iloc[:, [8, 9]].values
y = dataset.iloc[:, 4].values

# Splitting the dataset into the Training set and Test set & Feature Scaling
PrepareForPrediction(X, y)

# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

# Visualising the Training set results
visualizeResults(X_train, y_train)


# Visualising the Test set results
visualizeResults(X_test, y_test)

# good prediction ratio = 0.50194

# Apparently, the number of people accommodated at the place
# (or maximum number of people, that can be accommodated) 
# is a better indicator of the popularity of accommodations.
# It seems quite reasonalbe: "number of guests" is a factor we
# usualy filter the places by most usually. "Number of bedrooms"
# is a filter that is more hidden on the Airbnb site and thus
# maybe less commonly used.

# In general, as anticipated, the number of guests is a variable
# positively correlated with the popularity of places. However,
# places with small number of accommodations aren't excluded from
# people's choice. 
# What is more importnt here is price. Judging by the plot, it
# is obvious that the lower the price, the higher the probability
# of chosing a specific place. A bit higher price is accepted
# only when the place can accomomdate high number of guests.
    

