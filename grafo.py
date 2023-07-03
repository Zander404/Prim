class Grafo:

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[] for i in range(self.vertices)]

    def adcionar_aresta(self, u, v, peso):
        # Para grafos direcionados
        self.grafo[u - 1].append([v, peso])

        # Para grafos não direcionados
        self.grafo[v - 1].append([u, peso])

    def mostra_lista(self):
        for i in range(self.vertices):
            print(f'{i + 1}:', end='  ')
            for j in self.grafo[i]:
                print(f'{j} -> ', end='  ')

            print('')