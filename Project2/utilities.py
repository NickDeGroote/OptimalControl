import numpy as np
from typing import List
from scipy.spatial import distance_matrix


def create_distance_matrix(coords_list: List):
    x_coords = []
    y_coords = []
    for point in coords_list:
        x_coords.append(coords_list[0])
        y_coords.append(coords_list[1])
    dm = distance_matrix(x_coords, y_coords)
    return dm
