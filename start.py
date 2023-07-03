import heapq
import random

n, m - input().split()          #ler nº de vertices e arestas
n = int(n)
m = int(m)

H = []
n_out = [ []*n for i in range(n)]

for j in range(m):              #ler as m arestas do dígrafo
    a, b, c = input() .split()  #ler arestas de a para b com custo minimo
    a = int(a)
    b = int(b)
    c = int(c)
    n_out[a].append((b,c))
    n_out[b].append((a,c))

raiz = random.randint(0,n-1)    #pega valor aleatorio qlq entre 0 e n-1
for (x,c) in n_out[raiz]:       #inicializa o heap com as candidatas    
    heapq.heappush(H, (c, raiz, x))#insere no heap h uma aresta d custo c q vai da raiz até x

n_edges = 0                     #o numero de arestas da arvore é 0 
custo_tot = 0
marcados = [raiz]
arv_ger_min = []

while n_edges < n-1:
    while True:
        (c, a, b) = heapq.heappop(H)
        if b not in marcados: 
            break
    marcados.append(b)
    print(a,b)
    print(marcados)
    custo_tot += c
    arv_ger_min.append((a,b))
    n_edges += 1
    for (x,c) in n_out[b]:
        if x not in marcados:
            heapq.heappush(H, (c, b, x))

print(custo_tot)
print(arv_ger_min)