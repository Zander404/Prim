import random
import networkx as nx


def generate_random_edgelist(num_nodes, num_edges, weight_range=(1, 10)):
    if num_nodes <= 0:
        raise ValueError("Number of nodes must be greater than 0.")

    edges = []
    nodes = set(range(1, num_nodes + 1))

    while len(edges) < num_edges and len(nodes) > 1:
        u = random.choice(list(nodes))
        nodes.remove(u)
        v = random.choice(list(nodes))
        weight = random.randint(weight_range[0], weight_range[1])
        edges.append((u, v, weight))

    return edges
