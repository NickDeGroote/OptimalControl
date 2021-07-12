import time
import scipy.io

from Project2.nearest_neighbor import nearest_neighbor
from Project2.utilities import create_distance_matrix, plot_nn_route

"""
Test file for the Multi-Population Genetic Algorithm. A 50-dimensional 
Sphere Function is used with 5 populations to test the functionality.
"""

filename = 'test_files/us.mat'

mat = scipy.io.loadmat(filename)
city_list = mat["data"]
# Values refer to the PERCENTAGE of a one in a Chromosome for each population
# IMPORTANT: Each value must be between 0 and 100

# Start timer at current time
start_time = time.time()

route, dist = nearest_neighbor(city_list)

# Print the execution time of the MP GA
print("Run Time: %s seconds" % (time.time() - start_time))

# Print the best Chromosomes from each Population
print("Population best Route:")
print(route)
print("Distance: {}".format(dist))

soln_string = ""
for city in route:
    soln_string += str(city) + " -> "
print(soln_string)
plot_nn_route(city_list, route)
