from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

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
        parent, n = stack.pop()
        yield parent, n
        new = set(g[n]) - enqueued
        enqueued |= new
        stack.extend([(n, child) for child in new])

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

def shortest_pathdfs(g, start, end):
    parents = {}
    for parent, child in dfs(g, start):
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

    #grafo de una casa con sus diferentes conexiones entre habitaciones    
    casa = {'Entrada':['Hall1', 'Jardin'],
          'Hall1':['Entrada','Estudio','Salon'],
          'Estudio':['Hall1'],
          'Salon':['Hall1','Comedor'],
          'Garage':['Jardin','CuartoJardin'],
          'WC1':['Hall2'],
          'Dormitorio1':['Hall2'],
          'Hall2':['WC1','Dormitorio1','Comedor','Dormitorio2'],
          'Comedor':['Hall2','Salon','Trastero','Cocina'],
          'Trastero':['Comedor','Barbacoa','CuartoJardin'],
          'CuartoJardin':['Jardin','Trastero','Garage'],
          'Barbacoa':['Jardin','Trastero'],
          'Cocina':['Comedor'],
          'Dormitorio2':['Hall2','Closet','WC2'],
          'Closet':['Dormitorio2','WC2','Hall2'],
          'WC2':['Hall2','Closet','Dormitorio2'],
          'Jardin':['Entrada','Barbacoa','CuartoJardin','Garage']}

    GR=nx.Graph()
    for clave, valor in casa.items():
        for i in valor:
            GR.add_edge(clave, i)
        
    graficarG(GR, 0, "Grafo de Casa")

    #Grafica el grafo de casa despues de aplicar bfs y dfs
    casaBFS = crearGrafoBfS(casa,"Entrada", 0)
    graficarG(casaBFS, 0, "Grafo de Casa con BFS")
    casaDFS = crearGrafoDfS(casa,"Entrada", 0)
    graficarG(casaDFS, 0, "Grafo de Casa con DFS")


    ubi = input('Digite la habitacion en donde se encuentra el objeto perdido:       ')

    #solucion del camino de la busqueda del objeto
    lista = shortest_pathbfs(casa,"Entrada",ubi)
    casaSol = solucion(lista)
    graficarG(casaSol, 1, "Solucion de Casa con BFS")

    lista2 = shortest_pathdfs(casa,"Entrada",ubi)
    casaSol2 = solucion(lista2)
    graficarG(casaSol2, 1, "Solucion de Casa con DFS")


    h2 = h_lugares_comunes(casa, "Entrada", ubi)
    print("Resultado de heuristica 2, busqueda de lugares comunes (BFS).")
    print(h2)

