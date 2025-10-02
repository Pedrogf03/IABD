class Grafo:
    def __init__(self, num_ciudades=0):
        self.CIUDADES = num_ciudades
        self.adyacencia = {}

    def agregar_ciudad(self, ciudad):
        if ciudad not in self.adyacencia:
            self.adyacencia[ciudad] = {}
            self.CIUDADES += 1

    def agregar_carretera(self, origen, destino, distancia):
        self.agregar_ciudad(origen)
        self.agregar_ciudad(destino)
        self.adyacencia[origen][destino] = distancia
        self.adyacencia[destino][origen] = distancia  # grafo no dirigido

    def mostrar_conexiones(self, ciudad):
        if ciudad not in self.adyacencia:
            print(f"{ciudad} no está en el grafo.")
            return False
        print(f"\nDesde {ciudad} se puede llegar a:")
        for destino, distancia in self.adyacencia[ciudad].items():
            print(f"  - {destino}: {distancia} km")

    def dfs_util(self, ciudad, visitados):
        visitados.append(ciudad)
        print("'" + ciudad + "'", end=' ')
        for vecino in self.adyacencia[ciudad]:
            if vecino not in visitados:
                self.dfs_util(vecino, visitados)

    def dfs(self, ciudad):
        visitados = []
        self.dfs_util(ciudad, visitados)

    def bfs(self, ciudad):
        visitados = []
        cola = []
        cola.append(ciudad)
        visitados.append(ciudad)
        while cola:
            ciudad = cola.pop(0)
            print("'" + ciudad + "'", end=' ')
            for vecino in self.adyacencia[ciudad]:
                if vecino not in visitados:
                    cola.append(vecino)
                    visitados.append(vecino)

    def dijkstra(self, origen, destino):
        if origen not in self.adyacencia:
            print(f"{origen} no está en el grafo.")
            return False
        if destino not in self.adyacencia:
            print(f"{destino} no está en el grafo.")
            return False
        
        # En Dijkstra, las dintancias siempre empiezan en infinito.
        distancias = {ciudad: float('inf') for ciudad in self.adyacencia} # Diccionario ciudad - distancia.
        distancias[origen] = 0 # La distancia hasta el origen siempre es 0, ya que partimos de ahí.
        
        prev = {ciudad: None for ciudad in self.adyacencia} # Diccionario ciudad - ciudad anterior (para reconstruir la ruta a la inversa).
        
        no_visitadas = list(self.adyacencia.keys()) # Lista de ciudades aún no visitadas
        
        while no_visitadas: # Mientras queden ciudades por visitar:
            min_dist = float('inf')
            ciudad_actual = None
            for ciudad in no_visitadas: # Por cada ciudad no visitada:
                if distancias[ciudad] < min_dist: # Si la distancia a la ciudad es menor que la distancia minima:
                    min_dist = distancias[ciudad] # Se actualiza la distancia minima.
                    ciudad_actual = ciudad # Se actualiza la ciudad actual.
            
            # Si no se puede llegar a ninguna ciudad, se sale.
            if ciudad_actual is None: 
                break
            
            # Si se ha llegado a otra ciudad, se quita de la lista de no visitados.
            no_visitadas.remove(ciudad_actual)
            
            # Si la ciudad actual es el destino, salimos.
            if ciudad_actual == destino:
                break;
            
            # Se recorren las ciudades adyacentes a la ciudad actual con su distancia (actualizar distancias).
            for vecino, distancia in self.adyacencia[ciudad_actual].items():
                if vecino in no_visitadas:
                    # Calcular distancia alternativa
                    # (Recorrido desde origen a la ciudad actual + distancia desde la ciudad actual al vecino).
                    alt = distancias[ciudad_actual] + distancia
                    if alt < distancias[vecino]: # Si la distancia alternativa es menor que la distancia que ya teníamos:
                        distancias[vecino] = alt # Se actualiza la lista de distancias con la nueva que se ha calculado.
                        prev[vecino] = ciudad_actual # Guardamos como paso previo de vecino la ciudad actual.
        
        # En caso de que la distancia sea infinita:
        if distancias[destino] == float('inf'):
            print(f"No existe camino de {origen} a {destino}.")
            return False

        # Se reconstruye el camino en orden inverso.
        camino = []
        nodo = destino
        while nodo is not None: # El origen no tiene ciudad previa, por lo que cuando nodo sea 'None', habremos llegado al origen.
            camino.append(nodo) # Añadimos al camino la ciudad actual.
            nodo = prev[nodo] # Viajamos a la ciudad previa para continuar.
        camino.reverse() # Invertimos el camino
        
        print(f"Distancia mínima de {origen} a {destino}: {distancias[destino]} km")
        print("Camino:", " -> ".join(camino))

# -------------------------------------------------------------------------------------------------------------------------------------------------------

grafo = Grafo()
grafo.agregar_carretera("Cádiz", "San Fernando", 14)
grafo.agregar_carretera("Cádiz", "Puerto Real", 18)
grafo.agregar_carretera("Cádiz", "Jerez", 36)
grafo.agregar_carretera("San Fernando", "Chiclana", 10)
grafo.agregar_carretera("Puerto Real", "Jerez", 22)
grafo.agregar_carretera("Chiclana", "Conil", 17)
grafo.agregar_carretera("Conil", "Vejer", 16)
grafo.agregar_carretera("Vejer", "Medina Sidonia", 20)
grafo.agregar_carretera("Medina Sidonia", "Jerez", 34)
grafo.agregar_carretera("Jerez", "Arcos", 31)

print("\nRecorrido BFS desde Cádiz: ")
grafo.bfs("Cádiz")
print("\n")
print("\nRecorrido DFS desde Cádiz: ")
grafo.dfs("Cádiz")

print("\n")
print("\nRecorrido Dijkstra desde Cádiz hasta Vejer: ")
grafo.dijkstra("Cádiz", "Vejer")