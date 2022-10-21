from collections import deque
import networkx as nx
import matplotlib.pyplot as plt
import time

def bfs(g, start):
    queue, enqueued = deque([(None, start)]), set([start])
    while queue:
        parent, n = queue.popleft()
        yield parent, n
        new = set(g[n]) - enqueued
        enqueued |= new
        queue.extend([(n, child) for child in new])

def dfs(g, start):
    stack, enqueued = [(None, start)], set([start])
    while stack:
        print(stack)
        parent, n = stack.pop()
        yield parent, n
        new = set(g[n]) - enqueued
        enqueued |= new
        stack.extend([(n, child) for child in new])

def shortest_pathbfs(g, start, end):
    cont=0
    parents = {}
    for parent, child in bfs(g, start):
        parents[child] = parent
        if child == end:
            revpath = [end]
            while True:
                parent = parents[child]
                revpath.append(parent)
                cont=cont+1
                if parent == start:
                    break
                child = parent
            #print("La distancia en nodos es de: ", cont)
            return list(reversed(revpath))
    return None

def shortest_pathdfs(g, start, end):
    cont=0
    parents = {}
    for parent, child in dfs(g, start):
        parents[child] = parent
        if child == end:
            revpath = [end]
            while True:
                parent = parents[child]
                revpath.append(parent)
                cont=cont+1
                if parent == start:
                    break
                child = parent
            #print("La distancia en nodos es de: ", cont)
            return list(reversed(revpath))
    return None

def h_lugares_comunes(g, start, h_objeto):
    lug_c = ["Dormitorio2", "Comedor", "Estudio", "Garage"]
    claves = g.keys()
    for aux in lug_c:
        lista_res = shortest_pathbfs(g, start, aux)
        if h_objeto == lista_res[-1]: #interesa evaluar la ultima posicion
            return lista_res
    for aux in claves:
        if aux == "Entrada" or aux in lug_c:
            continue
        lista_res = shortest_pathbfs(g, start, aux)
        if h_objeto == lista_res[-1]: #interesa evaluar la ultima posicion
            return lista_res
    return None

def h_lugares_comunes2(g, start, h_objeto):
    lug_c = ["Dormitorio2", "Comedor", "Estudio", "Garage"]
    claves = g.keys()
    for aux in lug_c:
        lista_res = shortest_pathdfs(g, start, aux)
        if h_objeto == lista_res[-1]: #interesa evaluar la ultima posicion
            return lista_res
    for aux in claves:
        if aux == "Entrada" or aux in lug_c:
            continue
        lista_res = shortest_pathdfs(g, start, aux)
        if h_objeto == lista_res[-1]: #interesa evaluar la ultima posicion
            return lista_res
    return None

def crearGrafoDfS(graph, start, flag): #1 es dirigido y cualquier otro no dirigido
    claves = graph.keys()#extraer nodos de grafo original
    if(flag == 1):
        G = nx.DiGraph() #crear grafo 
    else:
        G = nx.Graph()
    for n in claves:
        G.nodes(n)

    for i in dfs(graph, start): #agregar aristas conforme algoritmo dfs
        if(i[0] == None):
            sus = i[1]
            continue 
        G.add_edge(i[0], i[1])

    if(flag == 1):
        i = 1
        for p, c, w in G.edges(data=True):#colocar el numero de pasos para llegar al nodo
            if(p != sus):
                if(G.has_edge(sus, p)):
                    i += 1
                w['weight'] = i
            else:
                w['weight'] = i
            sus = p
    return G

def crearGrafoBfS(graph, start, flag):
    claves = graph.keys()#extraer nodos de grafo original
    if(flag == 1):
        G = nx.DiGraph() #crear grafo 
    else:
        G = nx.Graph()
    for n in claves:
        G.nodes(n)

    for i in bfs(graph, start): #agregar aristas conforme algoritom dfs
        if(i[0] == None):
            sus = i[1]
            continue 
        G.add_edge(i[0], i[1])

    if(flag == 1):
        i = 1
        for p, c, w in G.edges(data=True):#colocar el numero de pasos para llegar al nodo
            if(p != sus):
                if(G.has_edge(sus, p)):
                    i += 1
                w['weight'] = i
            else:
                w['weight'] = i
            sus = p

    return G

def solucion(lista):  #graficar grafo con camino más corto
    G = nx.DiGraph()
    G.add_nodes_from(lista)
    for i in range(len(lista)-1):
        G.add_edge(lista[i], lista[i+1], weight=i+1)
    return G

def graficarG(g, flag, titulo):
    pos = nx.shell_layout(g)
    print(g.edges)
    if(flag == 1):
        labels = nx.get_edge_attributes(g, 'weight')
        nx.draw_networkx_edge_labels(g,pos,edge_labels=labels)
    nx.draw(g, pos, with_labels=True, node_color='gray', font_weight='bold', font_color='purple')
    plt.title(titulo)
    plt.show()
    

if __name__ == '__main__':
    # a sample graph
    graph = {'1': ['2', '3','5'],
             '2': [],
             '3': ['4'],
             '4': [],
             '5': ['3', '4'],
             '6': ['1', '7'],
             '7': ['6', '8'],
             '8': []}

    #Grafica el grafo de casa despues de aplicar bfs y dfs
    casaBFS = crearGrafoBfS(casa,"Entrada", 0)
    graficarG(casaBFS, 0, "Grafo de Casa con BFS")
    casaDFS = crearGrafoDfS(casa,"Entrada", 0)
    graficarG(casaDFS, 0, "Grafo de Casa con DFS")
