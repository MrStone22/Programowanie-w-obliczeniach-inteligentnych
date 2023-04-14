import os
import numpy as np
import pandas as pd
from PIL import Image
from skimage.feature import graycomatrix, graycoprops
import random
from matplotlib import pyplot as plt
from sklearn import svm

data = pd.read_csv('data.csv')  # read data from csv file
texture_types = data['category'].unique()
print(texture_types)
# TODO: Napisać skrypt do klasyfikacji wektorów cech z wykorzystaniem dowolnego algorytmu
# klasyfikacji danych dostępnego w pakiecie scikit-learn (np. support vector machines
# https://www.youtube.com/watch?v=efR1C6CvhmE&t=355s , K nearest
# neighbors). Uczenie przeprowadzić dla wyodrębnionego zbioru treningowego,
# a testowanie dla  zbioru testowego.
# #Obliczyć i wyświetlić na ekranie wyznaczoną dokładność klasyfikatora
