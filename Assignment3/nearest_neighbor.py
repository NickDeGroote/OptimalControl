from copy import copy


def nearest_neighbor(graph: dict, start: str, stop: str):
    """
    :param node_list: A list of the nodes in the graph
    :param graph: The nodes and their distances in the full graph
    :param start: The source node
    :param stop: The target node
    :return: The shorted route from the start to stop nodes
    """
    graph = copy(graph)
    current_node = start  # Current node is the start
    route = []  # Initialize route to empty
    while current_node != stop:  # Loop unt
        route.append(current_node)  # Add the current node to the route
        neighbors = graph[current_node]  # Get the neighbors of the current node
        min_dist = float("inf")  # Initialize minimum distance to infinity
        closest_node = None  # Initialize closest node to None
        for neighbor in neighbors:  # Loop through all neighbors
            if neighbor not in route:  # Check to make sure neighbor has not been visited
                dist = graph[current_node][neighbor]  # Check distance to neighbor
                if dist < min_dist:
                    min_dist = dist  # Found closet neighbor
                    closest_node = neighbor
        current_node = closest_node
    route.append(current_node)  # Add final node to route
    return route
