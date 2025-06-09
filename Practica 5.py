import matplotlib.pyplot as plt
import networkx as nx
import time

class Edge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight

    def __repr__(self):
        return f"{self.u} -- {self.weight} -- {self.v}"

class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            self.parent[root_v] = root_u
            return True
        return False

def graficar_grafo(vertices, edges, mst_edges=[], title="Grafo"):
    G = nx.Graph()
    G.add_nodes_from(vertices)
    pos = nx.spring_layout(G, seed=42)

    for edge in edges:
        G.add_edge(edge.u, edge.v, weight=edge.weight)

    edge_labels = {(e.u, e.v): e.weight for e in edges}
    colors = ['red' if (e.u, e.v) in [(m.u, m.v) for m in mst_edges] or (e.v, e.u) in [(m.u, m.v) for m in mst_edges] else 'gray' for e in edges]

    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, edge_color=colors, node_color='skyblue', node_size=700, font_size=14)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title(title)
    plt.show()

def kruskal_grafico(vertices, edges, modo='minimo'):
    print(f"\nSimulación del Árbol de {'Mínimo' if modo == 'minimo' else 'Máximo'} Costo usando Kruskal (con gráfica)\n")

    edges = sorted(edges, key=lambda edge: edge.weight, reverse=(modo == 'maximo'))
    ds = DisjointSet(vertices)
    mst = []
    costo_total = 0

    graficar_grafo(vertices, edges, [], "Grafo original")

    for edge in edges:
        print(f"Evaluando arista: {edge}")
        if ds.union(edge.u, edge.v):
            mst.append(edge)
            costo_total += edge.weight
            print(f"   ✅ Agregada. Costo acumulado: {costo_total}")
            graficar_grafo(vertices, edges, mst, f"Paso con arista {edge.u}-{edge.v}")
        else:
            print(f"   ❌ Rechazada (formaría ciclo)")

    print("\nÁrbol de expansión generado:")
    for e in mst:
        print(f" - {e}")
    print(f"\nCosto Total: {costo_total}")

    graficar_grafo(vertices, edges, mst, f"Árbol de {'mínimo' if modo == 'minimo' else 'máximo'} costo final")

# Ejemplo
vertices = ['A', 'B', 'C', 'D', 'E']
edges = [
    Edge('A', 'B', 1),
    Edge('A', 'C', 5),
    Edge('B', 'C', 4),
    Edge('B', 'D', 3),
    Edge('C', 'D', 2),
    Edge('C', 'E', 6),
    Edge('D', 'E', 7)
]

kruskal_grafico(vertices, edges, modo='minimo')
# Para árbol de máximo costo, solo cambia el modo:
# kruskal_grafico(vertices, edges, modo='maximo')
