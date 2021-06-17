import matplotlib.pyplot as plt
from typing import List
from Project2.ga.Chromosome import Chromosome
from scipy.spatial import distance_matrix


def create_distance_matrix(coords_list: List):
    x_coords = []
    y_coords = []
    for point in coords_list:
        x_coords.append(point[0])
        y_coords.append(point[1])
    dm = distance_matrix(coords_list, coords_list)
    return dm


def plot_route(city_list: list, route: Chromosome):
    x_coords = []
    y_coords = []

    for city in route.genes:
        x_coords.append(city_list[city][0])
        y_coords.append(city_list[city][1])
    x_coords.append(city_list[route.genes[0]][0])
    y_coords.append(city_list[route.genes[0]][1])
    plt.plot(x_coords, y_coords)
    plt.plot(city_list[0][0], city_list[0][1], 'r*', markersize = 15)
    plt.plot(x_coords, y_coords, 'o')
    plt.show()
