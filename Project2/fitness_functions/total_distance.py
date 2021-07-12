import numpy as np
from typing import List


def total_distance(route: List[int], dist_matrix: np.ndarray) -> float:
    total_dist = 0
    for city, next_city in zip(route, route[1:]):
        total_dist += dist_matrix[city, next_city]
    total_dist += dist_matrix[route[-1], route[0]]
    fitness = 1 / total_dist
    return fitness
