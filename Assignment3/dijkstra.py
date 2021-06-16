from copy import copy


def dijkstra(node_list: list, graph: dict, start: str, stop: str):
    """
    :param node_list: A list of the nodes in the graph
    :param graph: The nodes and their distances in the full graph
    :param start: The source node
    :param stop: The target node
    :return: The shorted route from the start to stop nodes
    """
    dist = {}  # Dictionary of distances to nodes
    previous_node = {}  # Dictionary of previous nodes
    node_list = copy(node_list)
    for vertex in node_list:
        dist[vertex] = float("inf")  # Initialize distances to infinity
        previous_node[vertex] = None  # Initialize previous nodes to None
    dist[start] = 0  # Set the distance to the starting node to be zero
    while bool(node_list):  # Loop until all nodes have been removed from the list
        current_node = min(dist, key=dist.get)  # Get the closet node to the current
        node_list.remove(current_node)  # Remove the current node from the list
        neighbors = graph[current_node]  # Get the neighbors of the current node
        for neighbor in neighbors:
            alt = dist[str(current_node)] + graph[current_node][neighbor]  # Distance to neighbors
            if neighbor in node_list:  # If the neighbor has not yet been visited
                if alt < dist[neighbor]:  # If this route is better than the current best
                    dist[neighbor] = alt  # Update distances dictionary
                    previous_node[neighbor] = current_node  # Update previous nodes dictionary
        dist.pop(current_node)  # Remove the current node from distances dictionary
    final_route = get_route(start, stop, previous_node)  # Determine the optimal path
    return final_route


def get_route(start: str, stop: str, prev: dict):
    """
    :param start: The source node
    :param stop: The target node
    :param prev: The dictionary of previous nodes
    :return: The optimal route
    """
    route = []  # Initialize route
    current_node = stop  # Set the current node to be the target node
    if prev[current_node] is not None or start == current_node:
        while current_node is not None:  # Loop until current node is None
            route.insert(0, current_node)  # Add the node to the list
            current_node = prev[current_node]  # Update current node
    return route
