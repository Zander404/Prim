import networkx as nx


def prim(grafo, raiz):
    vertices = list(nx.nodes(grafo))
    custo = {}
    predecessor = {}
    custo[raiz] = 0

    while vertices:

        u = min(custo, key=custo.get)
        for v in grafo.neighbors(u):
            if v in vertices:
                if not v in custo:
                    custo[v] = grafo[v][u]['weight']
                    predecessor[v] = u
                else:
                    if custo[v] > grafo[v][u]['weight']:
                        custo[v] = grafo[v][u]['weight']
                        predecessor[v] = u

        custo.pop(u)
        vertices.remove(u)

    caminho = []

    for v in predecessor:
        caminho.append((v, predecessor[v], grafo[v][predecessor[v]]['weight']))

    MST = nx.Graph()
    MST.add_weighted_edges_from(caminho)

    return MST
