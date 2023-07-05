import random

import networkx as nx
import prim as mst
import matplotlib.pyplot as plt
from grafo import generate_random_edgelist
"""
Gerar o grafo com seus pesos
"""

nodes = int(input("Quantos vertices vc deseja? "))
edge = int(input("Quantos arestas vc deseja? "))

random_list = generate_random_edgelist(nodes, edge, weight_range=(1, 10))

filename = 'sukita.txt'

with open(filename, 'w') as file:
    for u, v, weight in random_list:
        file.write(f"{u} {v} {weight}\n")

g = nx.read_edgelist(filename, create_using=nx.Graph(), nodetype=int, data=(('weight', int),))
sp = nx.spring_layout(g)

arestas = nx.get_edge_attributes(g, 'weight')

root = random.choice(list(g.nodes))

plt.axis('on')
nx.draw_networkx(g, sp, with_labels=True)
nx.draw_networkx_edge_labels(g, sp, edge_labels=arestas)
plt.show()

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
