import numpy as np
import pandas as pd
from sklearn import svm
from sklearn import metrics
from sklearn.model_selection import train_test_split

features = []
labels = []
properties_from_file = ['dissimilarity', 'correlation', 'contrast', 'energy', 'homogeneity', 'ASM']

pkl_file = pd.read_pickle('data.pkl')       # read features from .pkl file
textures = pkl_file['category'].unique()    # extraction of unique values

# rewriting data from pickle to tables: features and labels
for texture in textures:
    # select only this rows when there is a current texture name in the category column
    name = pkl_file[pkl_file['category'] == texture]
    # save properties from selected rows
    properties = name[properties_from_file]

    for i in properties.values:
        labels.append(texture)          # save texture name for each sample in labels table
        stacked = np.hstack(i)          # stack arrays horizontally to make a single array [1,2] [3,4] -> [1,2,3,4]
        flatten = stacked.flatten()     # create array collapsed into one dimension
        features.append(flatten)        # save flatten table to features

# split dataset into training set and test set
x_train, x_test, y_train, y_test = train_test_split(features, labels)

# create a svm Classifier
clf = svm.SVC(kernel='linear')

# train the model using the training sets
clf.fit(x_train, y_train)

# predict the response for test dataset
y_pred = clf.predict(x_test)

# model accuracy: how often is the classifier correct?
print('Accuracy:', round(metrics.accuracy_score(y_test, y_pred) * 100, 2), '%')
