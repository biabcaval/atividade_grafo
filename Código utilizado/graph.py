# -*- coding: utf-8 -*-
import queue

class Graph:
    def __init__(self, n):
        self.num_vertices = n
        self.matrix = [[0 for _ in range(n)] for _ in range(n)]
        self.list = [[] for _ in range(n)]
        

    def print(self):
        print(self.matrix)
        print(self.list)

    def print_adjs(self):
        print("Lista de anjacências")
        for i in range(self.num_vertices):
            print("{} - {}".format(i, self.list[i]))
        
        
    def bfs(self, source):
        dist = [-1 for _ in range(self.num_vertices)]
        ant = [-1 for _ in range(self.num_vertices)]
        isVisited = [False for _ in range(self.num_vertices)]
        Q = queue.Queue()
        Q.put(source)
        isVisited[source] = True
        dist[source] = 0 # o no inicial começa com dist 0
        
        while Q.empty() != True:
            p = Q.get() # "pop"
            print("Vertice: " + str(p))
            
            for v in self.list[p]:
                if isVisited[v] == False:
                    dist[v] = dist[p] + 1
                    ant[v] = p
                    Q.put(v)
                    isVisited[v] = True
        
        return dist, ant
    


def load_from(fileName):
    f = open(fileName, 'r') #abre arquivo
    n = int(f.readline()) #le linha do arquivo
    
    g = Graph(n) # cria grafo
    
    l = 0

    # /t é um char de espaço em branco
    for line in f:
        #print(line)
        #print("ola")
        line = line.strip()# tira espaços em branco no inicio e no final da string
        numeros = line.split("\t") # cria uma lista separada por "\t"
        c = 0
        for i in numeros:
            if(c == g.num_vertices): # Se o num da coluna for igual ao número de vertices, parar
                break
            #print(i)
            g.matrix[l][c] = int(i)
            if(g.matrix[l][c] > 0):
                g.list[l].append(c)
            
            c += 1
        l += 1
    return g
