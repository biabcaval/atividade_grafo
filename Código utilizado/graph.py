# -*- coding: utf-8 -*-
import queue
from collections import deque

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
        
    #BFS   
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
    

       # Parte recursiva que visita cada "filho" de um pai 
    def dfs_rec(self, v, isVisited, pai):
        isVisited[v] = True
        print(v, end=" ")
        for u in self.list[v]:
            if(isVisited[u] == False): # Se não visitado ainda, visite
                pai[u] = v
                self.dfs_rec(u, isVisited, pai)
    
    def dfs(self):
        isVisited = [False for _ in range(self.num_vertices)]
        pai = [-1 for _ in range(self.num_vertices)]

        for u in range(self.num_vertices):
            if(isVisited[u] == False):
                self.dfs_rec(u,isVisited,pai)
            return pai
    
    # método que conta o número de composições conexas no grafo
    def num_com_conex(self):
        pai = self.dfs()
        num = 0

        for u in range(self.num_vertices):
            if(pai[u] == -1):
                num +=1
            return num
     # método de busca DFS sem a parte recursiva  
    def dfs_sem_rec(self, inicio):
        isVisited = [False for _ in range(self.num_vertices)]
        stack = deque()
        pai = [-1 for _ in range(self.num_vertices)]

        isVisited[inicio] = True
        stack.append(inicio)

        while stack:
            s = stack.pop()
            print(s, end = " ")

            for n in reversed(self.list[s]):
                if isVisited[n] == False:
                    isVisited[n] = True
                    pai[n] = s
                    stack.append(n)
                
        return pai


        


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
