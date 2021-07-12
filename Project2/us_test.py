import time
import scipy.io

from Project2.fitness_functions.total_distance import total_distance
from Project2.ga.MP_Genetic_Algorithm import GeneticAlgorithm
from Project2.utilities import create_distance_matrix, plot_route

"""
Test file for the Multi-Population Genetic Algorithm. A 50-dimensional 
Sphere Function is used with 5 populations to test the functionality.
"""

filename = 'test_files/us.mat'

mat = scipy.io.loadmat(filename)
city_list = mat["data"]
distance_matrix = create_distance_matrix(city_list)

# Values refer to the PERCENTAGE of a one in a Chromosome for each population
# IMPORTANT: Each value must be between 0 and 100

# Start timer at current time
start_time = time.time()

# Create the MP GA object
ga = GeneticAlgorithm(
    input_data=distance_matrix,
    fitness_function=total_distance,
    population_size=75,
    generations=2500,
    crossover_probability=0.6,
    mutation_probability=0.03,
    elitism_ratio=0.02,
)

# Run the MP GA
ga.run()
# Get the best Chromosome from the MP GA run
best_chromosome = ga.get_best_chromosome()

# Print the execution time of the MP GA
print("Run Time: %s seconds" % (time.time() - start_time))

# Print the best Chromosomes from each Population
print("Population best Chromosome - (Fitness, [Genes]):")
print(best_chromosome)
print("Distance: {}".format(1 / best_chromosome.fitness))

ga.generate_plots()

plot_route(city_list, best_chromosome)
