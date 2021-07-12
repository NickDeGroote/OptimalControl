from copy import copy
import numpy as np


def nearest_neighbor(city_list):
    unvisited = city_list.tolist()
    city_list = city_list.tolist()
    route = []
    total_distance = 0
    city = unvisited[0]
    route.append(city_list.index(city))
    while unvisited:
        unvisited.remove(city)
        if not unvisited:
            break
        min_dist = float("inf")
        closest_city = None
        for city2 in unvisited:
            dist = np.sqrt( (city[0] - city2[0]) ** 2 + ( city[1] - city2[1] ) ** 2)
            if dist < min_dist:
                min_dist = dist
                closest_city = city2
        city = closest_city
        total_distance += min_dist
        route.append(city_list.index(closest_city))
    total_distance += np.sqrt( (city_list[0][0] - closest_city[0]) ** 2 + ( city_list[0][1] - city2[1] ) ** 2)

    return route, total_distance
