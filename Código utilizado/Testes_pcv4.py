from graph import Graph
from graph import load_from
from caminho import caminho
import queue

#teste bfs

g = load_from("pcv4.txt") # transforma o arquivo passado em uma estrutura grafo

print("\n BFS")
g.print_adjs()
dist, ant = g.bfs(3)# passa como parâmetro o valor a ser considerado inicial
print(dist)
print(ant)
caminho("pcv4.txt",3,0) # FILE, ORIGEM, DESTINO


#teste DFS

print("\n DFS")
print("Utilizando recursividade")
print(g.dfs())
print("Utilizando pilha")
print(g.dfs_sem_rec(0))
