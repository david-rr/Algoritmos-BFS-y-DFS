# Algoritmos-BFS-y-DFS
Implementación de los algoritmos de búsqueda en un grafo no dirigido. 
El programa genera una visualización del grafo de entrada y posteriormente muestra el resultante al aplicar los algoritmos de busqueda para generar el camino más corto hacia un nodo. Usando la siguiente función obtenemos el camino:

``` python
def shortest_pathbfs(g, start, end):
    parents = {}
    for parent, child in bfs(g, start):
        parents[child] = parent
        if child == end:
            revpath = [end]
            while True:
                parent = parents[child]
                revpath.append(parent)
                if parent == start:
                    break
                child = parent
            return list(reversed(revpath))
    return None
```

Para la parte grafica se hace uso de la libreria networkx la cual nos permite trabajar con grafos y matplotlib para dibujar los nodos y aristas con la siguiente función:
``` python
def graficarG(g, flag, titulo):
    pos = nx.shell_layout(g)
    print(g.edges)
    if(flag == 1):
        labels = nx.get_edge_attributes(g, 'weight')
        nx.draw_networkx_edge_labels(g,pos,edge_labels=labels)
    nx.draw(g, pos, with_labels=True, node_color='gray', font_weight='bold', font_color='purple')
    plt.title(titulo)
    plt.show()
```


Representacion de las conexiones existentes en la casa.

![image of home](https://user-images.githubusercontent.com/116386764/197304478-4690db01-d7d7-43a3-a283-57caa34af5f1.png)


El primer caso se aplica de manera general por lo que el primer resultado mostrado es un grafo con el camino mas corto usando **BFS y DFS** con nodo inicial en Entrada y se desglosa hacia todas las habitaciones.

![image short bfs](https://user-images.githubusercontent.com/116386764/197304711-e21bd446-c845-45f2-8eab-bd0fa9191b56.png)

El programa tambien muestra el camino más corto indicando el nodo inicial y el nodo final siendo introducido en teclado por el usuario.

![image](https://user-images.githubusercontent.com/116386764/197309296-ae80c493-dc53-4549-9d51-72394faa58d0.png)

