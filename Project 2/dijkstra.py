from graph import Graph
import heapq


def dijkstra_matrix(graph: Graph, start_vertex: int):
    """
    Dijkstra's algorithm to find the shortest path from start_vertex to all other vertices.
    Use an array for the priority queue.

    Parameters:
        graph (Graph): The input graph represented as an adjacency matrix.
        start_vertex (int): The starting vertex for the algorithm.
    Returns:
        list: A list of shortest distances from start_vertex to all other vertices.
    """

    if graph.representation != "adjacency_matrix":
        raise ValueError("Dijkstra's algorithm requires an adjacency matrix.")

    # Initialize distances and visited set
    distances = [float("inf")] * graph.vertices
    distances[start_vertex] = 0
    visited = [False] * graph.vertices

    for _ in range(graph.vertices):
        # Find the vertex with the minimum distance
        min_distance = float("inf")
        min_vertex = -1
        for v in range(graph.vertices):
            if not visited[v] and distances[v] < min_distance:
                min_distance = distances[v]
                min_vertex = v

        # Mark the vertex as visited
        visited[min_vertex] = True

        # Update distances for adjacent vertices
        for v in range(graph.vertices):
            if (
                graph.adj_matrix[min_vertex][v] > 0
                and not visited[v]
                and distances[min_vertex] + graph.adj_matrix[min_vertex][v]
                < distances[v]
            ):
                distances[v] = distances[min_vertex] + graph.adj_matrix[min_vertex][v]

    return distances


def dijkstra_list(graph: Graph, start_vertex: int):
    """
    Dijkstra's algorithm to find the shortest path from start_vertex to all other vertices.
    Use a min heap for the priority queue.

    Parameters:
        graph (Graph): The input graph represented as an adjacency list.
        start_vertex (int): The starting vertex for the algorithm.
    Returns:
        list: A list of shortest distances from start_vertex to all other vertices.
    """
    if graph.representation != "adjacency_list":
        raise ValueError("Dijkstra's algorithm requires an adjacency list.")

    # Initialize distances and visited set
    distances = [float("inf")] * graph.vertices
    distances[start_vertex] = 0
    visited = [False] * graph.vertices

    # Min-heap for priority queue
    min_heap = [(0, start_vertex)]  # (distance, vertex)

    while min_heap:
        # Extract the vertex with the minimum distance
        current_distance, min_vertex = heapq.heappop(min_heap)

        if visited[min_vertex]:
            continue

        # Mark the vertex as visited
        visited[min_vertex] = True

        # Update distances for adjacent vertices
        for v, weight in graph.adj_list[min_vertex]:
            if not visited[v] and current_distance + weight < distances[v]:
                distances[v] = current_distance + weight
                heapq.heappush(min_heap, (distances[v], v))

    return distances
