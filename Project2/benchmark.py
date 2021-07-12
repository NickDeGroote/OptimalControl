import time
import random
import scipy.io

from Project2.fitness_functions.total_distance import total_distance
from Project2.ga.MP_Genetic_Algorithm import GeneticAlgorithm
from Project2.utilities import create_distance_matrix, plot_route

"""
Test file for the Multi-Population Genetic Algorithm. A 50-dimensional 
Sphere Function is used with 5 populations to test the functionality.
"""

all_distances = []
all_run_times = []

for i in range(0, 50):

    filename = 'test_files/config' + str(i+1) + '.mat'
    mat = scipy.io.loadmat(filename)

    print("\nTest #{} - File: {}".format(i, filename))

    # Random list of cities
    city_list = mat["rand_config"]
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
        mutation_probability=0.05,
        elitism_ratio=0.02,
        verbose=False,
    )

    # Run the MP GA
    ga.run()
    # Get the best Chromosome from the MP GA run
    best_chromosome = ga.get_best_chromosome()

    run_time = time.time() - start_time
    # Print the execution time of the MP GA
    print("Run Time: %s seconds" % run_time)

    # Print the best Chromosomes from each Population
    print("Population best Chromosome - (Fitness, [Genes]):")
    print(best_chromosome)
    print("Distance: {}".format(1 / best_chromosome.fitness))
    all_distances.append(1 / best_chromosome.fitness)
    all_run_times.append(run_time)

print("\nAverage Distance:")
print(sum(all_distances) / len(all_distances))
print(sum(all_run_times) / len(all_run_times))
