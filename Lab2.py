import matplotlib.pyplot as plt
import numpy as np
import csv
from sklearn.cluster import KMeans
from scipy.stats import norm


def read_csv(file_name):                     # read data from csv
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for x_csv, y_csv, z_csv in reader:
            yield float(x_csv), float(y_csv), float(z_csv)  # returns a line of the csv file as a tuple


def load_cloud(file_name):
    cloud = []
    for i in read_csv(file_name):
        cloud.append(i)
    return cloud


def load_clouds():
    clouds_from_csv = []
    clouds_from_csv.extend(load_cloud('floorCloud.xyz'))
    clouds_from_csv.extend(load_cloud('wallCloud.xyz'))
    clouds_from_csv.extend(load_cloud('cylinderCloud.xyz'))
    return clouds_from_csv


clouds = load_clouds()  # load previously generated point plane files
x, y, z = zip(*clouds)  # unzip 3 axis variables from clouds

plt.figure()    # plot clouds
ax = plt.axes(projection='3d')
ax.scatter3D(x, y, z)
plt.show()

# find disjoint point clouds using k-means algorithms for k=3
X = np.array(clouds)
clusterer = KMeans(n_init=10, n_clusters=3)        # create clusterizer object
clusterer.fit(X)                                   # passing data to clusterizer
predicted_index = clusterer.predict(X)             # predicting a label for a cloud of points

red = predicted_index == 0       # translation of cluster index to color
blue = predicted_index == 1
green = predicted_index == 2

plt.figure()    # plot the results
plt.title('Results of K-mean')
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
