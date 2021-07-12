from scipy.spatial import ConvexHull
from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt

filename = 'test_files/us.mat'

mat = loadmat(filename)
city_list = mat["data"]

hull = ConvexHull(city_list)

for simplex in hull.simplices:
    plt.plot(city_list[simplex,0], city_list[simplex,1], 'k-')

plt.plot(city_list[:,0], city_list[:,1], 'o')
plt.show()