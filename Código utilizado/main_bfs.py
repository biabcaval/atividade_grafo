# -*- coding: utf-8 -*-
from graph import Graph
import queue

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


gr = load_from("pcv4.txt")
gr.print()
gr.print_adjs()
dist, ant = gr.bfs(3)# passa como parâmetro o valor a ser considerado inicial
print(dist)
print(ant)


