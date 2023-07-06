import random
import networkx as nx


def generate_random_graph(num_nodes, num_edges, weight_range=(1, 10)):
    if num_nodes <= 0 or num_edges <= 0:
        raise ValueError("Number of nodes and edges must be greater than 0.")

    # Create an empty graph
    g = nx.Graph()

    # Add nodes to the graph
    g.add_nodes_from(range(1, num_nodes + 1))

    # Add random edges to the graph
    for _ in range(num_edges):
        u = random.randint(1, num_nodes)
        v = random.randint(1, num_nodes)
        while u == v or g.has_edge(u, v):
            u = random.randint(1, num_nodes)
            v = random.randint(1, num_nodes)
        weight = random.randint(weight_range[0], weight_range[1])
        g.add_edge(u, v, weight=weight)

    return g