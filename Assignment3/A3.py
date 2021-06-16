from Assignment3.dijkstra import dijkstra
from Assignment3.nearest_neighbor import nearest_neighbor


vertices = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]  # List of all vertices
graph = {  # Graph of vertices and distances
    "1": {"2": 16, "3": 10, "4": 25},
    "2": {"1": 16, "3": 20, "4": 3, "5": 15},
    "3": {"1": 10, "2": 20, "4": 40, "6": 6},
    "4": {"1": 25, "2": 3, "3": 40, "5": 11, "6": 32},
    "5": {"2": 15, "4": 11, "6": 22, "7": 27, "8": 19},
    "6": {"3": 6, "4": 32, "5": 22, "7": 16, "9": 28},
    "7": {"4": 23, "5": 27, "6": 16, "8": 30, "9": 10},
    "8": {"5": 19, "7": 30, "9": 25, "10": 14},
    "9": {"6": 28, "7": 10, "8": 25, "10": 9},
    "10": {"8": 14, "9": 9},
}

dijkstra_route = dijkstra(vertices, graph, "1", "10")  # Run Dijkstra's Algorithm
nn_route = nearest_neighbor(graph, "1", "10")
print(dijkstra_route)  # Print the final route
print(nn_route)
