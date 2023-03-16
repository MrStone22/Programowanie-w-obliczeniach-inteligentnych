from scipy.stats import norm
from csv import writer


def create_floor_cloud(numberOfPoints=2000):
    # create continuous random variable
    # loc - mean, scale - standard deviation
    distribution_x = norm(loc=0, scale=200)
    distribution_y = norm(loc=0, scale=200)
    distribution_z = norm(loc=0.2, scale=0.5)

    # create random variable?
    x = distribution_x.rvs(size=numberOfPoints)
    y = distribution_y.rvs(size=numberOfPoints)
    z = distribution_z.rvs(size=numberOfPoints)

    points = zip(x, y, z)   # create iterator of tuples based on the iterable objects

    # zapis wyników do pliku csv
    with open('floorCloud.xyz', 'w', encoding='utf-8', newline='\n') as csvfile:
        csvfile = writer(csvfile)
        for p in points:
            csvfile.writerow(p)


def create_wall_cloud(numberOfPoints=2000):
    # create continuous random variable
    # loc - mean, scale - standard deviation
    distribution_x = norm(loc=0.2, scale=0.5)
    distribution_y = norm(loc=0, scale=200)
    distribution_z = norm(loc=0, scale=200)

    # create random variable?
    x = distribution_x.rvs(size=numberOfPoints)
    y = distribution_y.rvs(size=numberOfPoints)
    z = distribution_z.rvs(size=numberOfPoints)

    points = zip(x, y, z)   # create iterator of tuples based on the iterable objects

    # zapis wyników do pliku csv
    with open('wallCloud.xyz', 'w', encoding='utf-8', newline='\n') as csvfile:
        csvfile = writer(csvfile)
        for p in points:
            csvfile.writerow(p)


def create_cylinder_cloud(numberOfPoints=2000):
    # create continuous random variable
    # loc - mean, scale - standard deviation
    distribution_x = norm(loc=0, scale=200)
    distribution_y = norm(loc=0, scale=200)
    distribution_z = norm(loc=0.2, scale=500)

    # create random variable?
    x = distribution_x.rvs(size=numberOfPoints)
    y = distribution_y.rvs(size=numberOfPoints)
    z = distribution_z.rvs(size=numberOfPoints)

    points = zip(x, y, z)   # create iterator of tuples based on the iterable objects

    # zapis wyników do pliku csv
    with open('cylinderCloud.xyz', 'w', encoding='utf-8', newline='\n') as csvfile:
        csvfile = writer(csvfile)
        for p in points:
            csvfile.writerow(p)


create_floor_cloud(20000)
create_wall_cloud(20000)
create_cylinder_cloud(20000)

print('done')
