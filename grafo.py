class Grafo:

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0]*self.vertices for i in range(self.vertices)]

    def adcionar_aresta(self, u, v, peso):
        # Para grafos direcionados
        self.grafo[u - 1][v-1] = 1

        # Para grafos não direcionados
        self.grafo[v - 1][u - 1] = 1

    def mostrar_matriz(self):
        for i in range(self.vertices):
            print(self.grafo[i])
