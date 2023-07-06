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
arestas = nx.get_edge_attributes(g, 'weight')

plt.axis('on')
nx.draw_networkx(g, sp, with_labels=True)
nx.draw_networkx_edge_labels(g, sp, edge_labels=arestas)
plt.show()

#ordernar os vertices
nodes = sorted(g.nodes())

# Pegar o numero de arestas
num_nodes = len(nodes)

# criar um matriz vazia
adj_matrix = np.zeros((num_nodes, num_nodes), dtype=int)

# Preencher com 1 as posições onde tem uma aresta ligando os vertices
for u, v in g.edges():
    i = nodes.index(u)
    j = nodes.index(v)
    adj_matrix[i, j] = 1
    adj_matrix[j, i] = 1


print('Matriz de Adjacencia')

for i in range(num_nodes):
    row_str = " ".join(str(adj_matrix[i, j]) for j in range(num_nodes))
    print(f"{nodes[i]}: {row_str}")

print("\n\n")

arestas = nx.get_edge_attributes(g, 'weight')


"""
Matriz Custo
"""

cost_matrix = np.zeros((num_nodes, num_nodes), dtype=int)

print('Matriz de Custo')

for u, v, data in g.edges(data=True):
    i = nodes.index(u)
    j = nodes.index(v)
    weight = data['weight']
    cost_matrix[i, j] = weight
    cost_matrix[j, i] = weight

for i in range(num_nodes):
    row_str = " ".join(str(cost_matrix[i, j]) for j in range(num_nodes))
    print(f"{nodes[i]}: {row_str}")

print('\n\n')


"""
Gerar Arvore MST
"""

while True:
    try:
        root = int(input("Qual será a Vértice Raiz?"))
        break
    except ValueError:
        print("Valor Digitado é inválido!!!")


MST = mst.prim(g, root)
sp = nx.spring_layout(MST)
plt.axis('off')
nx.draw_networkx(MST, sp, with_labels=True)
nx.draw_networkx_edge_labels(MST, sp, edge_labels=arestas)
plt.show()
