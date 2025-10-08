import networkx as nx

G = nx.Graph()

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

# BFS
bfs_recorrido = list(nx.bfs_tree(G, source="Cádiz").nodes())
print("\nRecorrido BFS desde Cádiz:", bfs_recorrido)

# DFS
dfs_recorrido = list(nx.dfs_tree(G, source="Cádiz").nodes())
print("Recorrido DFS desde Cádiz:", dfs_recorrido)

# Dijkstra
camino = nx.dijkstra_path(G, source="Cádiz", target="Vejer", weight="distancia")
print("Recorrido Dijkstra desde Cádiz a Vejer:", camino)

distancia_total = 0
print("\nDistancia tramo a tramo:")
for i in range(len(camino)-1):
    origen = camino[i]
    destino = camino[i+1]
    distancia = G[origen][destino]['distancia']
    distancia_total += distancia
    print(f"{origen} -> {destino}: {distancia} km")

print("\nDistancia total del camino:", distancia_total, "km")