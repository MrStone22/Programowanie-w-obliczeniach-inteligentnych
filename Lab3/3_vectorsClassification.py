import os
import numpy as np
import pandas as pd
from PIL import Image
from skimage.feature import graycomatrix, graycoprops
import random
from matplotlib import pyplot as plt
from sklearn import svm
from sklearn import metrics
from sklearn.model_selection import train_test_split

data = pd.read_csv('data.csv')  # read data from csv file
texture_types = data['category'].unique()


# A # cancer.data  table
# B # cancer.target table in table

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(A, B, test_size=0.3, random_state=109) # 70% training and 30% test

# Create a svm Classifier
clf = svm.SVC(kernel='linear') # Linear Kernel

# Train the model using the training sets
clf.fit(X_train, y_train)


# Predict the response for test dataset
y_pred = clf.predict(X_test)

# Model Accuracy: how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

# TODO: Napisać skrypt do klasyfikacji wektorów cech z wykorzystaniem dowolnego algorytmu
# klasyfikacji danych dostępnego w pakiecie scikit-learn (np. support vector machines
# https://www.youtube.com/watch?v=efR1C6CvhmE&t=355s , K nearest
# neighbors). Uczenie przeprowadzić dla wyodrębnionego zbioru treningowego,
# a testowanie dla  zbioru testowego.
# #Obliczyć i wyświetlić na ekranie wyznaczoną dokładność klasyfikatora
