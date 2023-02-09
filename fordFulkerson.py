import numpy as np
import graph
import sys

def main():

    # Le poids des arcs de ce graphe correspondent aux capacités
    g = example()

    # Le poids des arcs de ce graphe correspondent au flot
    flow = fordFulkerson(g, "s", "t")

    print(flow)
    
# Fonction créant un graphe sur lequel sera appliqué l'algorithme de Ford-Fulkerson
def example():
        
    g = graph.Graph(np.array(["s", "a", "b", "c", "d", "e", "t"]))

    g.addArc("s", "a", 8)
    g.addArc("s", "c", 4)
    g.addArc("s", "e", 6)
    g.addArc("a", "b", 10)
    g.addArc("a", "d", 4)
    g.addArc("b", "t", 8)
    g.addArc("c", "b", 2)
    g.addArc("c", "d", 1)
    g.addArc("d", "t", 6)
    g.addArc("e", "b", 4)
    g.addArc("e", "t", 2)
    
    return g

# Fonction appliquant l'algorithme de Ford-Fulkerson à un graphe
# Les noms des sommets sources est puits sont fournis en entrée
def fordFulkerson(g, sName, tName):

    """
    Marquage des sommets du graphe:
     - mark[i] est égal à +j si le sommet d'indice i peut être atteint en augmentant le flot sur l'arc ji
     - mark[i] est égal à  -j si le sommet d'indice i peut être atteint en diminuant le flot de l'arc ji
     - mark[i] est égal à sys.float_info.max si le sommet n'est pas marqué
    """
    mark = [sys.float_info.max] * g.n

    # Récupérer l'indice de la source et du puits
    s = g.indexOf(sName)
    t = g.indexOf(tName)
    
    # Créer un nouveau graphe contenant les même sommets que g
    flow = graph.Graph(g.nodes) # will contain the flows -> initially is equal to 0
    flow_list = [] # is going to store the amount of capacity that can be better at each node

    # Récupérer tous les arcs du graphe 
    arcs = g.getArcs()

    # Ajouter votre code ici
    # finding the first flot

    for i in g.nodes:
        if mark[t] == sys.float_info.max:
            index_i = g.indexOf(i)
            marked = False
            mark[s] = '+'
            for j in g.nodes:
                index_j = g.indexOf(j)
                if not marked:
                    if g.adjacency[index_i, index_j] > 0:
                        if (mark[index_j] == sys.float_info.max) and (mark[index_i] != sys.float_info.max) and flow.adjacency[index_i, index_j] != g.adjacency[index_i, index_j]:
                            mark[index_j] = + index_i
                            marked = True
                            flow_list.append(g.adjacency[index_i, index_j])
                            if index_j == t:
                                cap_imp = min(flow_list)
                                for i_m in range(len(mark)):
                                    if mark[i_m] != '+' and mark[i_m] != sys.float_info.max:
                                        flow.adjacency[mark[i_m], i_m] = cap_imp

    flow_list = []  # is going to store the amount of capacity that can be better at each node

    # after first one was chosen
    while(mark[t] != sys.float_info.max):
        mark = [sys.float_info.max] * g.n
        mark[s] = "+"

        for i in g.nodes:
            if mark[t] == sys.float_info.max:
                index_i = g.indexOf(i)
                marked = False
                for j in g.nodes:
                    index_j = g.indexOf(j)
                    if not marked:
                        if g.adjacency[index_i, index_j] > 0:
                            if (mark[index_j] == sys.float_info.max) and (mark[index_i]!= sys.float_info.max) and flow.adjacency[index_i,index_j]!=g.adjacency[index_i,index_j]:
                                mark[index_j] = + index_i
                                marked = True
                                flow_list.append(g.adjacency[index_i,index_j] - flow.adjacency[index_i,index_j])
                                if index_j == t:
                                    cap_imp = min(flow_list)
                                    for i_m in range(len(mark)):
                                        if mark[i_m] != '+' and mark[i_m] != sys.float_info.max:
                                            flow.adjacency[mark[i_m], i_m] = cap_imp
                                            flow_list = []

                            if (mark[index_i] == sys.float_info.max) and (mark[index_j] != sys.float_info.max) and (flow.adjacency[index_j,index_i] != 0):
                                mark[index_i] = - index_j
                                marked = True
                                flow_list.append(flow.adjacency[index_j, index_i])


    return flow
   
if __name__ == '__main__':
    main()
