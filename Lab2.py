import matplotlib.pyplot as plt
import numpy as np
import csv

from sklearn.cluster import KMeans
from scipy.stats import norm

# wczytać poprzednio wygenerowane pliki z płaszczyzną punktów


def read_csv(file_name):                     # generator ładujący dane z pliku csv
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for x, y, z in reader:
            yield float(x), float(y), float(z)  # zwraca wiersz pliku csv w postaci krotki


def load_cloud(file_name):
    clouds = []
    for i in read_csv(file_name):
        clouds.append(i)
    x, y, z = zip(*clouds)
    return x, y, z


x, y, z = load_cloud('wallCloud.xyz')

plt.figure()
plt.scatter(y, z)
plt.show()

# znaleźć rozłączne chmury punktów za pomocą algorytmów k-średnich dla k=3
# X = np.array(clusters)
# clusterer = KMeans(n_init=3)    # utworzenie obiektu klasteryzatora
# clusterer.fit(X)                    # przekazanie danych do klasteryzatora
# y_pred = clusterer.predict(X)       # przewidzenie etykiety dla chmury punktów
#
# red = y_pred == 0       # oznaczanie kolorów 13 min
# blue = y_pred == 1
# green = y_pred == 2

# plt.figure()
# plt.scatter3D(X[red, 0], X[red, 1], X[red, 2], color="red")
# plt.scatter3D(X[blue, 0], X[blue, 1], X[blue, 2], color="blue")
# plt.scatter3D(X[green, 0], X[green, 1], X[green, 2], color="green")
# plt.show()



# dla każdej chmury przeprowadzić próbę dopasowania za pomocą algorytmu RANSAC

# wypisać na ekranie współrzędne wektora normalnego do znalezionej płaszczyzny

# określić czy chmura jest płaszczyzną (np. na podstawie średniej odległości wszystkich punktów chmury do
# tej płaszczyzny)

#  jeśli jest płaszczyzną, czy ta płaszczyzna jest pionowa, czy pozioma.

# Zainstalować pakiet pyransac3d

# opcje