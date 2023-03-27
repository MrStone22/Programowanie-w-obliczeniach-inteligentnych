import matplotlib.pyplot as plt
import numpy as np
import csv
from sklearn.cluster import KMeans
from scipy.stats import norm

# wczytać poprzednio wygenerowane pliki z płaszczyzną punktów


def read_csv(file_name):                     # read data from csv
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for x, y, z in reader:
            yield float(x), float(y), float(z)  # returns a line of the csv file as a tuple


def load_cloud(file_name):
    cloud = []
    for i in read_csv(file_name):
        cloud.append(i)
    return cloud


def load_clouds():
    clouds = []
    clouds.extend(load_cloud('floorCloud.xyz'))
    clouds.extend(load_cloud('wallCloud.xyz'))
    clouds.extend(load_cloud('cylinderCloud.xyz'))
    return clouds


clouds = load_clouds()
x, y, z = zip(*clouds)

plt.figure()
ax = plt.axes(projection='3d')
ax.scatter3D(x, y, z)
plt.show()

# znaleźć rozłączne chmury punktów za pomocą algorytmów k-średnich dla k=3
X = np.array(clouds)
print(len(clouds))
print(len(X))
clusterer = KMeans(n_init=10, n_clusters=3)        # utworzenie obiektu klasteryzatora
clusterer.fit(X)                    # przekazanie danych do klasteryzatora
y_pred = clusterer.predict(X)       # przewidzenie etykiety dla chmury punktów

red = y_pred == 0       # oznaczanie kolorów 13 min
blue = y_pred == 1
green = y_pred == 2

plt.figure()
ax = plt.axes(projection='3d')
ax.scatter3D(X[red, 0], X[red, 1], X[red, 2], color="red")
ax.scatter3D(X[blue, 0], X[blue, 1], X[blue, 2], color="blue")
ax.scatter3D(X[green, 0], X[green, 1], X[green, 2], color="green")
plt.show()


# dla każdej chmury przeprowadzić próbę dopasowania za pomocą algorytmu RANSAC

# wypisać na ekranie współrzędne wektora normalnego do znalezionej płaszczyzny

# określić czy chmura jest płaszczyzną (np. na podstawie średniej odległości wszystkich punktów chmury do
# tej płaszczyzny)

#  jeśli jest płaszczyzną, czy ta płaszczyzna jest pionowa, czy pozioma.

# Zainstalować pakiet pyransac3d

# opcje