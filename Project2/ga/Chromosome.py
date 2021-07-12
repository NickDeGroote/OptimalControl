import random
from typing import Callable, List

"""
Class for a Chromosome in the Genetic Algorithm
"""


class Chromosome:
    """
    Structure to hold the genes of an individual and its corresponding fitness
    """

    def __init__(self, genes: List[int]):
        self.genes = genes
        self.fitness = 0

    def mutate(self) -> None:
        """
        Mutates this Chromosome
        :return: None
        """
        mutation_type = random.randint(0, 2)
        if mutation_type == 0:
            # Swaps the value of a random gene in this Chromosome
            swapping_genes = random.sample(range(0, len(self.genes)), 2)
            self.genes[swapping_genes[0]], self.genes[swapping_genes[1]] = (
                self.genes[swapping_genes[1]],
                self.genes[swapping_genes[0]],
            )
        elif mutation_type == 1:
            swapping_genes = random.sample(range(0, len(self.genes)), 2)
            swapping_genes.sort()
            self.genes[swapping_genes[0]: swapping_genes[1]] = reversed(
                self.genes[swapping_genes[0]: swapping_genes[1]]
            )
        else:
            swapping_genes = random.sample(range(0, len(self.genes)), 2)
            swapping_genes.sort()
            temp_genes = self.genes[(swapping_genes[0] + 1): swapping_genes[1]]
            temp_genes.append(self.genes[swapping_genes[0]])
            self.genes[swapping_genes[0]: swapping_genes[1]] = temp_genes

    def calculate_fitness(self, fitness_function: Callable, data=None) -> float:
        """
        Calculates the fitness of this Chromosome
        :param fitness_function: Function evaluating fitness
        :return: Fitness of Chromosome
        """
        self.fitness = fitness_function(self.genes, data)
        return self.fitness

    def reorder_genes(self) -> None:
        zero_index = self.genes.index(0)
        part_1 = self.genes[:zero_index]
        part_2 = self.genes[zero_index:]
        self.genes = part_2 + part_1

    def __repr__(self):
        """
        Return Chromosome representation in human readable form.
        """
        return repr((self.fitness, self.genes))
