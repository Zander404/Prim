from grafo import Grafo
import networkx as nx
import prim as mst
import matplotlib.pyplot as plt


"""
Gerar o grafo com seus pesos
"""
g = nx.read_edgelist('sukita.txt', create_using=nx.Graph(), nodetype=int, data=(('weight', int),))
sp = nx.spring_layout(g)

arestas = nx.get_edge_attributes(g, 'weight')

plt.axis('on')
nx.draw_networkx(g, sp, with_labels=True)
nx.draw_networkx_edge_labels(g, sp, edge_labels=arestas)
plt.show()

"""
Gerar Arvore MST
"""

MST = mst.prim(g, 6)

arestas = nx.get_edge_attributes(MST, 'weight')

sp = nx.spring_layout(MST)
plt.axis('off')
nx.draw_networkx(MST, sp, with_labels=True)
nx.draw_networkx_edge_labels(MST, sp, edge_labels=arestas)
plt.show()
