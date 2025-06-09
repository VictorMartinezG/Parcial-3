import heapq
import networkx as nx
import matplotlib.pyplot as plt

# Definimos el grafo como un diccionario de listas de adyacencia
grafo = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 1)],
    'C': [('A', 3), ('B', 1), ('D', 4)],
    'D': [('B', 1), ('C', 4)]
}

def prim(grafo, inicio):
    visitado = set()              # Conjunto de nodos visitados
    mst = []                      # Lista de aristas del árbol mínimo
    total = 0                     # Costo total del MST
    heap = [(0, inicio, None)]    # Cola de prioridad con (peso, nodo, nodo_origen)

    print("== INICIO DEL ALGORITMO DE PRIM ==")
    while heap:
        peso, actual, anterior = heapq.heappop(heap)
        if actual in visitado:
            continue
        visitado.add(actual)

        if anterior:
            mst.append((anterior, actual, peso))
            total += peso
            print(f" Arista añadida: ({anterior}, {actual}) con peso {peso}")
        else:
            print(f" Comenzando desde el nodo: {actual}")

        for vecino, p in grafo[actual]:
            if vecino not in visitado:
                heapq.heappush(heap, (p, vecino, actual))
                print(f"   ↪ Se detecta arista candidata: ({actual}, {vecino}) con peso {p}")
    
    print("\n== MST COMPLETO ==")
    for a, b, p in mst:
        print(f"({a}, {b}) con peso {p}")
    print(f" Peso total del árbol: {total}")

    return mst

# Función para graficar el MST usando networkx y matplotlib
def graficar_mst(mst):
    G = nx.Graph()
    for a, b, p in mst:
        G.add_edge(a, b, weight=p)
    
    pos = nx.spring_layout(G, seed=42)  # Layout para una buena disposición
    etiquetas = nx.get_edge_attributes(G, 'weight')

    plt.figure(figsize=(6, 4))
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=etiquetas)
    plt.title("Árbol de Expansión Mínimo (Prim)", fontsize=14)
    plt.tight_layout()
    plt.show()

# Ejecutar el algoritmo y graficar el resultado
mst_resultado = prim(grafo, 'A')
graficar_mst(mst_resultado)
