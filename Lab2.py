import matplotlib.pyplot as plt
import numpy as np
import csv
from sklearn.cluster import KMeans, DBSCAN
import random
import math
import pyransac3d as pyrsc


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


def ransac(points, min_distance=0.5, iterations=50):
    inliers = []
    inliers_new = []
    outliers = []
    outliers_new = []

    while iterations:
        inliers_new.clear()
        outliers_new.clear()
        iterations -= 1

        # select 3 random points
        point1 = random.choice(points)
        point2 = random.choice(points)
        point3 = random.choice(points)

        # calculate the parameters of the plane equation: ax + by + cz + d = 0
        # a = (y2 - y1) * (z3 - z1) - (z2 - z1) * (y3 - y1)
        a = (point2[1] - point1[1]) * (point3[2] - point1[2]) - (point2[2] - point1[2]) * (point3[1] - point1[1])
        # b = (z2 - z1) * (x3 - x1) - (x2 - x1) * (z3 - z1)
        b = (point2[2] - point1[2]) * (point3[0] - point1[0]) - (point2[0] - point1[0]) * (point3[2] - point1[2])
        # c = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
        c = (point2[0] - point1[0]) * (point3[1] - point1[1]) - (point2[1] - point1[1]) * (point3[0] - point1[0])
        # d = -(a * x1 + b * y1 + c * z1)
        d = -(a * point1[0] + b * point1[1] + c * point1[2])

        divider = max(0.1, np.sqrt(a * a + b * b + c * c))  # calculate divider to distance calculations

        for point in points:
            # skip iteration if point is previously selected random point
            if point in point1 or point in point2 or point in point3:
                continue

            # calculate the distance between point and plane
            # distance = np.abs(a * point[0] + b * point[1] + c * point[2] + d) / divider
            distance = math.fabs(a * point[0] + b * point[1] + c * point[2] + d) / divider

            if distance <= min_distance:   # add the point to inliers if it's close enough to the plane
                inliers_new.append(point)
            else:
                outliers_new.append(point)

        # check if in this iterations we have more inliers than before if its true save results
        if len(inliers_new) > len(inliers):
            inliers.clear()
            outliers.clear()
            inliers = inliers_new
            outliers = outliers_new

    return inliers, outliers, a, b, c, d


clouds = load_clouds()  # load previously generated point plane files
x, y, z = zip(*clouds)  # unzip 3 axis variables from clouds

# plt.figure()    # plot clouds
# plt.title('Points')
# ax = plt.axes(projection='3d')
# ax.scatter3D(x, y, z)
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
# plt.show()

# find disjoint point clouds using k-means algorithms for k=3
X = np.array(clouds)
clusterer = KMeans(n_init=10, n_clusters=3)        # create clusterizer object
clusterer.fit(X)                                   # passing data to clusterizer
predicted_index = clusterer.predict(X)             # predicting a label for a cloud of points

red = predicted_index == 0       # translation of cluster index to color
blue = predicted_index == 1
green = predicted_index == 2

cloud1 = X[red]         # separate each cloud to new variable
cloud2 = X[blue]
cloud3 = X[green]

# plt.figure()    # plot the results
# plt.title('Results of K-mean')
# ax = plt.axes(projection='3d')
# ax.scatter3D(X[red, 0], X[red, 1], X[red, 2], color="red")
# ax.scatter3D(X[blue, 0], X[blue, 1], X[blue, 2], color="blue")
# ax.scatter3D(X[green, 0], X[green, 1], X[green, 2], color="green")
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
# plt.show()


# for each cloud perform a matching test using the RANSAC algorithm
plane_a = plane_b = plane_c = plane_d = 0

inl1, outl1, plane_a1, plane_b1, plane_c1, plane_d1 = ransac(cloud1, 0.5, 50)
x_inl1, y_inl1, z_inl1 = zip(*inl1)  # unzip 3 axis variables

inl2, outl2, plane_a2, plane_b2, plane_c2, plane_d2 = ransac(cloud2, 0.5, 50)
x_inl2, y_inl2, z_inl2 = zip(*inl2)  # unzip 3 axis variables

inl3, outl3, plane_a3, plane_b3, plane_c3, plane_d3 = ransac(cloud3, 0.5, 50)
x_inl3, y_inl3, z_inl3 = zip(*inl3)  # unzip 3 axis variables

# plt.figure()    # plot clouds
# plt.title('Results of RANSAC')
# ax = plt.axes(projection='3d')
# ax.scatter3D(x_inl1, y_inl1, z_inl1, color='red')
# ax.scatter3D(x_inl2, y_inl2, z_inl2, color='blue')
# ax.scatter3D(x_inl3, y_inl3, z_inl3, color='green')
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
# plt.show()

print('Vector 1 is: ', end='')   # print to console coordinates of the normal vector
print(str(plane_a1), str(plane_b1), str(plane_c1), sep='  ')
print('Vector 2 is: ', end='')   # print to console coordinates of the normal vector
print(str(plane_a2), str(plane_b2), str(plane_c2), sep='  ')
print('Vector 3 is: ', end='')   # print to console coordinates of the normal vector
print(str(plane_a3), str(plane_b3), str(plane_c3), sep='  ')


# określić czy chmura jest płaszczyzną (np. na podstawie średniej odległości wszystkich punktów chmury do # TODO
# tej płaszczyzny)

#  jeśli jest płaszczyzną, czy ta płaszczyzna jest pionowa, czy pozioma.


# Option 1
# use DBSCAN algorithm from scikit-learn and pyransac3d library
X2 = np.array(clouds)
db = DBSCAN(eps=3, min_samples=2).fit(X2)
labels = db.labels_

red = labels == 0       # translation of cluster index to color
blue = labels == 1
green = labels == 2

cloud1 = X2[red]         # separate each cloud to new variable
cloud2 = X2[blue]
cloud3 = X2[green]

x = np.linspace(-40, 20)   # create meshgrid to plot a plane # TODO: clear
y = np.linspace(-40, 20)
x, y = np.meshgrid(x, y)

plane1 = pyrsc.Plane()
best_eq1, best_inliers1 = plane1.fit(cloud1)
eq1 = best_eq1[0] * x + best_eq1[1] * y + best_eq1[2] + best_eq1[3]    # create plane equation

plane2 = pyrsc.Plane()
best_eq2, best_inliers2 = plane2.fit(cloud2)
eq2 = best_eq2[0] * x + best_eq2[1] * y + best_eq2[2] + best_eq2[3]    # create plane equation

plane3 = pyrsc.Plane()
best_eq3, best_inliers3 = plane3.fit(cloud3)
eq3 = best_eq3[0] * x + best_eq3[1] * y + best_eq3[2] + best_eq3[3]    # create plane equation

plt.figure()    # plot the results
plt.title('Results of DBSCAN and pyRANSAC-3D')
ax = plt.axes(projection='3d')
ax.scatter3D(X2[red, 0], X2[red, 1], X2[red, 2], color="red")
ax.scatter3D(X2[blue, 0], X2[blue, 1], X2[blue, 2], color="blue")
ax.scatter3D(X2[green, 0], X2[green, 1], X2[green, 2], color="green")
ax.plot_surface(x, y, eq1)
ax.plot_surface(x, y, eq2)
ax.plot_surface(x, y, eq3)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()

