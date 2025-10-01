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

while True:
  ciudad = input("\nIntroduce una ciudad de Cádiz ('fin' para terminar): ")
  if ciudad.lower() == "fin":
    break
  if grafo.mostrar_conexiones(ciudad) == False:
    continue
  print(f"Recorrido en anchura (comenzando en {ciudad}):")
  grafo.bfs(ciudad)
  print(f"\nRecorrido en profundidad (comenzando en {ciudad}):")
  grafo.dfs(ciudad)