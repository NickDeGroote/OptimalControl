import numpy as np
from typing import List


def total_distance(dist_matrix: np.ndarray, route: List[int]) -> float:
    total_dist = 0
    previous_city = route[0]
    for city in route[1:]:
        total_dist += dist_matrix[previous_city, city]
        previous_city = city
    total_dist += dist_matrix[previous_city, route[0]]
    fitness = 1 / total_dist
    return fitness
