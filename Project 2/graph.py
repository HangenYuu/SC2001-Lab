from typing import Literal


class Graph:
    def __init__(
        self,
        vertices: int,
        representation: Literal[
            "adjacency_list", "adjacency_matrix"
        ] = "adjacency_list",
    ):
        self.vertices = vertices
        self.representation = representation
        if representation == "adjacency_list":
            # Store (vertex, weight) pairs in adjacency list
            self.adj_list = [[] for _ in range(vertices)]
        elif representation == "adjacency_matrix":
            # Use matrix to store weights (0 means no edge)
            self.adj_matrix = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u: int, v: int, weight: float = 1.0):
        if self.representation == "adjacency_list":
            self.adj_list[u].append((v, weight))
            self.adj_list[v].append((u, weight))  # For undirected graph
        elif self.representation == "adjacency_matrix":
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight  # For undirected graph

    def remove_edge(self, u: int, v: int):
        if self.representation == "adjacency_list":
            # Find and remove the edge with vertex v
            self.adj_list[u] = [
                (vertex, weight) for vertex, weight in self.adj_list[u] if vertex != v
            ]
            self.adj_list[v] = [
                (vertex, weight) for vertex, weight in self.adj_list[v] if vertex != u
            ]
        elif self.representation == "adjacency_matrix":
            self.adj_matrix[u][v] = 0
            self.adj_matrix[v][u] = 0

    def __str__(self):
        result = []
        if self.representation == "adjacency_list":
            for i in range(self.vertices):
                result.append(f"{i}: {self.adj_list[i]}")
        elif self.representation == "adjacency_matrix":
            for row in self.adj_matrix:
                result.append(str(row))
        return "\n".join(result)

    def visualize(self):
        """Visualize the graph using Graphviz."""
        try:
            from graphviz import Graph as GVGraph
        except ImportError:
            print("Graphviz package not found. Install it with 'pip install graphviz'")
            return

        # Create a new graphviz graph
        G = GVGraph("G", format="png", engine="neato")

        # Add nodes
        for i in range(self.vertices):
            G.node(str(i), shape="circle", style="filled", fillcolor="lightblue")

        # Add edges with weights
        if self.representation == "adjacency_list":
            for u in range(self.vertices):
                for v, weight in self.adj_list[u]:
                    if u < v:  # Add each edge only once
                        G.edge(str(u), str(v), label=f"{weight:.1f}")
        elif self.representation == "adjacency_matrix":
            for u in range(self.vertices):
                for v in range(u + 1, self.vertices):
                    if self.adj_matrix[u][v] != 0:
                        G.edge(str(u), str(v), label=f"{self.adj_matrix[u][v]:.1f}")

        # Set graph attributes for better visualization
        G.attr(overlap="false")
        G.attr(splines="true")
        G.attr(nodesep="0.5")
        G.attr(ranksep="0.5")

        # Render and display the graph
        G.attr(label="Graph Visualization with Weights")
        G.attr(fontsize="16")

        return G
