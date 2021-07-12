import matplotlib.pyplot as plt
from typing import List

import numpy as np

from Project2.ga.Chromosome import Chromosome
from scipy.spatial import distance_matrix
from sklearn.cluster import KMeans


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


def plot_mtsp(clusters, best_chroms):


    for i in range(0, len(clusters)):
        x_coords = []
        y_coords = []
        for city in best_chroms[i].genes:
            x_coords.append(clusters[i][city][0])
            y_coords.append(clusters[i][city][1])
        x_coords.append(clusters[i][best_chroms[i].genes[0]][0])
        y_coords.append(clusters[i][best_chroms[i].genes[0]][1])
        plt.plot(x_coords, y_coords, '-o')
        plt.plot(clusters[i][0][0], clusters[i][0][1], 'r*', markersize = 15)
    plt.show()


def plot_nn_route(city_list: list, route: list):
    x_coords = []
    y_coords = []

    for city in route:
        x_coords.append(city_list[city][0])
        y_coords.append(city_list[city][1])
    x_coords.append(city_list[route[0]][0])
    y_coords.append(city_list[route[0]][1])
    plt.plot(x_coords, y_coords)
    plt.plot(city_list[0][0], city_list[0][1], 'r*', markersize = 15)
    plt.plot(x_coords, y_coords, 'o')
    plt.show()


def separate_clusters(num_clusters, city_list, depot, polar_coords = None):
    if polar_coords:
        kmeans = KMeans(n_clusters=num_clusters, random_state=0).fit(polar_coords)
    else:
        kmeans = KMeans(n_clusters=num_clusters, random_state=0).fit(city_list)
    clusters = [ [depot] for _ in range(num_clusters) ]
    for city, label in zip(city_list, kmeans.labels_):
        clusters[label].append(city.tolist())
    return clusters


def cart_to_polar(city_list: list, depot: list):
    polar_data = []
    for city in city_list:
        x = city[0] - depot[0]
        y = city[1] - depot[1]
        theta = np.arctan2(x, y)
        r = np.sqrt(x ** 2 + y ** 2)
        polar_data.append([r, theta])
    return polar_data