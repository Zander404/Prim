import random

import networkx as nx
import prim as mst
import matplotlib.pyplot as plt
from grafo import generate_random_graph
import numpy as np

"""
Gerar o grafo com seus pesos
"""

nodes = int(input("Quantos vertices vc deseja? "))
edge = int(input("Quantos arestas vc deseja? "))

random_list = generate_random_graph(nodes, edge, weight_range=(1, 10))

edge_list = list(random_list.edges(data=True))
filename = 'sukita.txt'

with open(filename, 'w') as file:
    for u, v, data in edge_list:
        weight = data['weight']
        file.write(f"{u} {v} {weight}\n")


g = nx.read_edgelist(filename, create_using=nx.Graph(), nodetype=int, data=(('weight', int),))
sp = nx.spring_layout(g)

adj_matrix = nx.adjacency_matrix(g).todense()

for row in adj_matrix:
    print(" ".join(map(str, row)).replace("0", " "), end="\n")


arestas = nx.get_edge_attributes(g, 'weight')
root = random.choice(list(g.nodes))

"""
Gerar Arvore MST
"""

MST = mst.prim(g, root)

arestas = nx.get_edge_attributes(MST, 'weight')

sp = nx.spring_layout(MST)
plt.axis('off')
nx.draw_networkx(MST, sp, with_labels=True)
nx.draw_networkx_edge_labels(MST, sp, edge_labels=arestas)
plt.show()
