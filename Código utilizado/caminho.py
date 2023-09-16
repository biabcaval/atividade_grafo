from graph import Graph
from graph import load_from
import queue


def caminho(file, origem, destino):
    caminho = []
    caminho.append(origem) # coloca a origem dentro do caminho

    g = load_from(file) # cria o grafo

    dist = [-1 for _ in range(g.num_vertices)]
    ant = [-1 for _ in range(g.num_vertices)]
    isVisited = [False for _ in range(g.num_vertices)]
    Q = queue.Queue()
    Q.put(origem)
    isVisited[origem] = True
    dist[origem] = 0 # o no inicial começa com dist 0
    
    while Q.empty() != True:
        p = Q.get() # "pop"
        
        if p == destino:
            if p not in caminho:
                caminho.append(p)
            print("O caminho é: ", caminho)
            return True

        for v in g.list[p]:  # Processo de BFS
            if isVisited[v] == False:
                dist[v] = dist[p] + 1
                ant[v] = p
                Q.put(v)
                isVisited[v] = True

                if destino in g.list[v] or v == destino: # Checa se o destino é vizinho do v analisado ou v é o próprio destino
                    if ant[v] not in caminho: # Evitando adicionar vertices extras que deixariam o caminho mais longo
                        caminho.append(ant[v])
    return False
    

