import random
import numpy as np
from csv import writer


# saving results to .xyz file
def write_csv(number_of_points, name='noname'):
    with open(name, 'w', encoding='utf-8', newline='\n') as csvfile:
        csvfile = writer(csvfile)
        for p in number_of_points:
            csvfile.writerow(p)


def create_surface_cloud(number_of_points=2000, x1=0, x2=1, y1=0, y2=1, z1=0, z2=0.05):
    x, y, z = [], [], []
    for _ in range(number_of_points):
        x.append(random.uniform(x1, x2))
        y.append(random.uniform(y1, y2))
        z.append(random.uniform(z1, z2))

    points = zip(x, y, z)  # create iterator of tuples based on the iterable objects
    return points


def create_cylinder_cloud(number_of_points=2000, radius=3, height=5, x_center=0, y_center=0, noise=0.05):
    x, y, z = [], [], []

    for i in range(number_of_points):
        r = random.uniform(radius-noise, radius)
        angle = random.uniform(-np.pi, np.pi)
        x.append(r * np.cos(angle) + x_center)
        y.append(r * np.sin(angle) + y_center)
        z.append(random.uniform(0, height))

    points = zip(x, y, z)  # create iterator of tuples based on the iterable objects
    return points


if __name__ == '__main__':
    cloud = create_surface_cloud(200, x1=-30, x2=-40, y1=0, y2=10, z1=0, z2=0.01)
    write_csv(cloud, 'floorCloud.xyz')
    cloud = create_surface_cloud(200, x1=0, x2=0.01, y1=30, y2=40, z1=0, z2=10)
    write_csv(cloud, 'wallCloud.xyz')
    cloud = create_cylinder_cloud(200)
    write_csv(cloud, 'cylinderCloud.xyz')
    print('done')