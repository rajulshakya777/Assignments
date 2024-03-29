# -*- coding: utf-8 -*-
"""MI_Activity1.1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_jwu4lGVoZ-XeAhInt9fRkRnjieF03l0
"""

from sklearn.datasets import load_iris;
iris_dataset = load_iris()

from sklearn.neighbors import KNeighborsClassifier;
knn = KNeighborsClassifier(n_neighbors=1);

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split( iris_dataset['data'], iris_dataset['target'], random_state=0);

print(X_test)

print(y_test)

knn.fit(X_train, y_train);

print("Test set score: {:.2f}".format(knn.score(X_test, y_test)))

