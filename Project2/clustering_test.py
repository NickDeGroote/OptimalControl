import time
import scipy.io

from Project2.fitness_functions.total_distance import total_distance
from Project2.ga.MP_Genetic_Algorithm import GeneticAlgorithm
from Project2.utilities import create_distance_matrix, plot_mtsp
from Project2.utilities import separate_clusters, cart_to_polar

"""
Test file for the Multi-Population Genetic Algorithm. A 50-dimensional 
Sphere Function is used with 5 populations to test the functionality.
"""

filename = 'test_files/us.mat'

mat = scipy.io.loadmat(filename)
city_list = mat["data"]

polar_coords = cart_to_polar(city_list, [0.75, 0.5])
clusters = separate_clusters(num_clusters=3, city_list=city_list, depot=[0.75, 0.5], polar_coords=polar_coords)

dist_matrices = []
for cluster in clusters:
    dist_matrices.append(create_distance_matrix(cluster))

best_chromosomes = []
for dist_matrix, cluster in zip(dist_matrices, clusters):
    # Start timer at current time
    start_time = time.time()
    # Create the MP GA object
    ga = GeneticAlgorithm(
        input_data=dist_matrix,
        fitness_function=total_distance,
        population_size=75,
        generations=1500,
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
    best_chromosomes.append(best_chromosome)

total_dist = 0
for chromosome in best_chromosomes:
    total_dist += (1 / chromosome.fitness)

print("\nTotal Distance: {}".format(total_dist))
plot_mtsp(clusters, best_chromosomes)
