import networkx as nx

# Crear grafo no dirigido
G = nx.Graph()

# Agregar ciudades y carreteras con distancia como peso
G.add_edge("Cádiz", "San Fernando", distancia=14)
G.add_edge("Cádiz", "Puerto Real", distancia=18)
G.add_edge("Cádiz", "Jerez", distancia=36)
G.add_edge("San Fernando", "Chiclana", distancia=10)
G.add_edge("Puerto Real", "Jerez", distancia=22)
G.add_edge("Chiclana", "Conil", distancia=17)
G.add_edge("Conil", "Vejer", distancia=16)
G.add_edge("Vejer", "Medina Sidonia", distancia=20)
G.add_edge("Medina Sidonia", "Jerez", distancia=34)
G.add_edge("Jerez", "Arcos", distancia=31)

# Mostrar conexiones de una ciudad
ciudad = "Chiclana"
print(f"\nDesde {ciudad} se puede llegar a:")
for vecino in G.neighbors(ciudad):
    distancia = G[ciudad][vecino]["distancia"]
    print(f"  - {vecino}: {distancia} km")

# BFS
bfs_recorrido = list(nx.bfs_tree(G, source="Chiclana").nodes())
print("\nRecorrido BFS desde Chiclana:", bfs_recorrido)

# DFS
dfs_recorrido = list(nx.dfs_tree(G, source="Chiclana").nodes())
print("Recorrido DFS desde Chiclana:", dfs_recorrido)
