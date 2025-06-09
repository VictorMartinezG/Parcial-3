# Importamos la librería tkinter para crear interfaces gráficas
import tkinter as tk
# Importamos networkx para manejar y visualizar grafos
import networkx as nx
# Importamos matplotlib para graficar el grafo
import matplotlib.pyplot as plt
# Importamos funciones adicionales de tkinter para diálogos y mensajes
from tkinter import simpledialog, messagebox
# Importamos heapq para usar colas de prioridad (necesario en Dijkstra)
import heapq

# Función que implementa el algoritmo de Dijkstra
def dijkstra(grafo, inicio):
    # Se inicializa un diccionario de distancias con infinito
    distancias = {nodo: float('inf') for nodo in grafo}
    # La distancia al nodo inicial es 0
    distancias[inicio] = 0
    # Diccionario para registrar el nodo anterior en el camino más corto
    previos = {nodo: None for nodo in grafo}
    # Cola de prioridad con el nodo inicial
    cola = [(0, inicio)]

    # Mientras haya nodos en la cola
    while cola:
        # Se obtiene el nodo con menor distancia
        distancia_actual, nodo_actual = heapq.heappop(cola)

        # Recorremos los vecinos del nodo actual
        for vecino, peso in grafo[nodo_actual]:
            # Calculamos la nueva distancia posible
            nueva_distancia = distancia_actual + peso
            # Si la nueva distancia es menor, actualizamos
            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                previos[vecino] = nodo_actual
                # Se agrega el vecino a la cola con su nueva distancia
                heapq.heappush(cola, (nueva_distancia, vecino))

    # Se retornan las distancias y los caminos más cortos
    return distancias, previos

# Función que reconstruye el camino más corto desde el nodo previo
def reconstruir_camino(previos, destino):
    camino = []  # Lista vacía para construir el camino
    actual = destino  # Empezamos desde el destino
    while actual:  # Mientras haya un nodo válido
        camino.insert(0, actual)  # Insertamos al inicio de la lista
        actual = previos[actual]  # Retrocedemos al nodo previo
    return camino  # Retornamos el camino reconstruido

# Diccionario que representa el grafo con sus conexiones y pesos
grafo = {
    'A': [('B', 2), ('C', 4)],
    'B': [('A', 2), ('C', 1), ('D', 7)],
    'C': [('A', 4), ('B', 1), ('D', 3)],
    'D': [('B', 7), ('C', 3)]
}

# Creamos un grafo con NetworkX
G = nx.Graph()
# Añadimos las aristas y pesos al grafo
for nodo, conexiones in grafo.items():
    for vecino, peso in conexiones:
        G.add_edge(nodo, vecino, weight=peso)

# Función que dibuja el grafo con o sin camino resaltado
def mostrar_grafo(camino=None):
    pos = nx.spring_layout(G)  # Calcula posición de nodos para visualización
    pesos = nx.get_edge_attributes(G, 'weight')  # Extrae los pesos de las aristas

    # Creamos figura
    plt.figure(figsize=(8, 6))
    # Dibujamos nodos y aristas
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1000,
            font_size=14, font_weight='bold')
    # Dibujamos etiquetas de los pesos
    nx.draw_networkx_edge_labels(G, pos, edge_labels=pesos)

    # Si hay un camino, lo dibujamos en rojo
    if camino:
        edges_camino = list(zip(camino, camino[1:]))  # Creamos lista de aristas del camino
        nx.draw_networkx_edges(G, pos, edgelist=edges_camino,
                               edge_color='red', width=3)  # Dibujamos aristas rojas

    # Título de la figura
    plt.title("Algoritmo de Dijkstra - Camino más corto")
    # Mostramos el grafo
    plt.show()

# Función que se ejecuta al presionar el botón
def ejecutar_dijkstra():
    # Pedimos al usuario el nodo de inicio
    inicio = simpledialog.askstring("Nodo de inicio", "¿Desde qué nodo quieres comenzar? (Ej. A, B, C...)")
    # Pedimos el nodo de destino
    destino = simpledialog.askstring("Nodo de destino", "¿A qué nodo quieres llegar? (Ej. D, C...)")

    # Verificamos que los nodos ingresados sean válidos
    if inicio in grafo and destino in grafo:
        # Ejecutamos el algoritmo
        distancias, previos = dijkstra(grafo, inicio)
        # Obtenemos el camino más corto
        camino = reconstruir_camino(previos, destino)

        # Construimos el mensaje con distancia y camino
        resultado = f"Distancia de {inicio} a {destino}: {distancias[destino]}\nCamino: {' -> '.join(camino)}"
        # Mostramos mensaje en una ventana emergente
        messagebox.showinfo("Resultado", resultado)
        # Mostramos visualmente el grafo con el camino en rojo
        mostrar_grafo(camino)
    else:
        # Si los nodos son inválidos, se muestra un error
        messagebox.showerror("Error", "Nodo inválido. Intenta con A, B, C o D.")

# Creamos la ventana principal de Tkinter
ventana = tk.Tk()
# Título de la ventana
ventana.title("Simulador Dijkstra - Puntos Extras")

# Botón que ejecuta el algoritmo al hacer clic
boton = tk.Button(ventana, text="Ejecutar Dijkstra", command=ejecutar_dijkstra,
                  font=('Arial', 14), padx=20, pady=10)
# Lo añadimos al layout
boton.pack(pady=30)

# Iniciamos el loop principal de la aplicación
ventana.mainloop()
