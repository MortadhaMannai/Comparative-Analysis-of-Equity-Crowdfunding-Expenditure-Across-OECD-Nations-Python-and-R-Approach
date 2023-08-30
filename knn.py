# K-Nearest Neighbors (K-NN)

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('airbnb_warsaw.csv',sep=';')
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

# Fitting K-NN to the Training set
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

# apparently, the K-NN method did slightly worse predicting the results
# than the logistic regression. The ratio of well-predicted outcomes in 
# Logistic Regression was 1,58 : 1, while in K-NN it was only 1,43 : 1.
# What's interesting is the fact that this prediction (with the result of 
# arount 1,4) was still much better then the one, where the dataset excluded 
# outliers - 2k PLN places with 0 bedrooms and zero reviews. There the 
# prediction ratio was at around 1,2 : 1).

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
    plt.title('K-NN')
    plt.xlabel('number of bedrooms')
    plt.ylabel('price in PLN')
    plt.legend()
    plt.show()


# Visualising the Training set results
visualizeResults(X_train, y_train)


# Visualising the Test set results
visualizeResults(X_test, y_test)

