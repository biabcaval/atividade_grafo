from graph import Graph
from graph import load_from


g = load_from("pcv4.txt")



lista_pais = g.dfs()
print(lista_pais)

print(g.dfs_sem_rec(0))