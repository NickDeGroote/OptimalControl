import random
import time
from operator import attrgetter
from typing import Callable, List, Tuple

import matplotlib.pyplot as plt

from Project2.ga.Chromosome import Chromosome
from Project2.ga.Population import Population

"""
Class for Multi-population (MP) Genetic Algorithm (GA)
"""


class GeneticAlgorithm:
    def __init__(
        self,
        input_data: float,
        fitness_function: Callable,
        population_size: int = 50,
        generations: int = 100,
        crossover_probability: float = 0.9,
        mutation_probability: float = 0.05,
        elitism_ratio: float = 0.1,
        verbose: bool = True,
    ):
        self.input_data = input_data
        self.fitness_function = fitness_function
        self.population_size = population_size
        self.num_generations = generations
        self.crossover_probability = crossover_probability
        self.mutation_probability = mutation_probability
        self.elitism_ratio = elitism_ratio
        self.population = None
        self.verbose = verbose

    def create_population(self) -> None:
        """
        Creates the populations for the first generation of the MP GA
        :return: Population object containing Chromosomes
        """

        self.population = Population(
            data=self.input_data,
            fitness_function=self.fitness_function,
            population_size=self.population_size,
            crossover_probability=self.crossover_probability,
            mutation_probability=self.mutation_probability,
            elitism_ratio=self.elitism_ratio,
        )
        self.population.create_chromosomes(self.input_data)

    def update_population(self) -> None:
        """
        Performs the intra Population operations for the GA
        :return: None
        """
        self.population.log_population_attributes()
        self.population.update_to_next_generation()

    def rank_population(self) -> None:
        """
        Ranks the Chromosomes in this Population by their respective fitness values
        :return: None
        """
        # Ranks Chromosomes by their "fitness" attribute
        self.population.sort(key=attrgetter("population_fitness"), reverse=True)

    def run(self) -> None:
        """
        Call to run the MP GA
        :return: None
        """
        self.create_population()
        for i in range(1, self.num_generations + 1):
            start_time = time.time()
            self.update_population()
            if self.verbose:
                # Perform migration every number of specified generations
                self.display_iteration_info(i, self.num_generations, start_time)

    def get_best_chromosome(self) -> Chromosome:
        """
        Returns the best Chromosome from each Population at the end of every generation
        :return: A Tuple of the best Chromosomes in each Population
        """
        best_chromosome = self.population.get_best_chromosome()
        return best_chromosome

    @staticmethod
    def display_iteration_info(current_gen: int, total_gens: int, start_time: float):
        delta_t = time.time() - start_time
        print(
            "Generation: {} / {}  -  Time: {:0.3f} seconds".format(
                current_gen, total_gens, delta_t
            )
        )

    def generate_plots(self) -> None:
        """
        Generates three plots over the lifecycle of the MP GA:
        1. Population Best Chromosome Fitness
        2. Population Average Fitness Over Generations
        3. Population Size Over Generations
        :return: None
        """
        fig1, ax1 = plt.subplots()
        fig2, ax2 = plt.subplots()

        best_chrom_fitnesses = []
        generations = []
        legends = []
        for generation in range(0, self.num_generations):
            generations.append(generation)
            best_chrom_fitnesses.append(
                self.population.best_chromosome_log[generation].fitness
            )
            legends.append("Population {}".format(generation))

        ax1.plot(generations, best_chrom_fitnesses)
        # The first average fitness is zero, ignore it
        ax2.plot(generations[1:], self.population.population_fitness_log[1:])
        ax1.title.set_text("Population Best Chromosome Fitness Over Generations")
        ax2.title.set_text("Population Average Fitness Over Generations")
        ax1.set_xlabel("Generation")
        ax2.set_xlabel("Generation")
        ax1.set_ylabel("Fitness")
        ax2.set_ylabel("Average Fitness")
        ax1.legend(legends)
        ax2.legend(legends)
        plt.show()
