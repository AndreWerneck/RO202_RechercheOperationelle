import numpy as np
import graph
import sys

def main():
    
    # Créer un graphe contenant les sommets a, b, c, d, e, f, g 
    # exo 3.3
    # g = graph.Graph(np.array(["a", "b", "c", "d", "e", "f", "g"]))

    # Créer un graphe contenant les sommets a, b, c, d, e, f, g ,h
    # exo 3.4 - graph 1
    # g = graph.Graph(np.array(["a", "b", "c", "d", "e", "f", "g","h"]))

    # exo 3.4 - graph
    g = graph.Graph(np.array(["a", "b", "c", "d", "e", "f"]))

    # #graph exercice 3.3
    # # Ajouter les arêtes
    # g.addEdge("a", "b",  1.0)
    # g.addEdge("a", "c",  8.0) # changed weight for 8, as the firs ex of the TD
    # g.addEdge("b", "c",  2.0)
    # g.addEdge("b", "d",  5.0)
    # g.addEdge("b", "e",  7.0)
    # g.addEdge("b", "f",  9.0)
    # g.addEdge("c", "d",  4.0)
    # g.addEdge("d", "e",  6.0)
    # g.addEdge("d", "g", 12.0)
    # g.addEdge("e", "f",  8.0)
    # g.addEdge("e", "g", 11.0)
    # g.addEdge("f", "g", 10.0)

    # graph 1 exercice 3.4
    # Ajouter les arêtes
    # g.addEdge("a", "b", 9.0)
    # g.addEdge("a", "f", 6.0)
    # g.addEdge("a", "h", 9.0)
    # g.addEdge("b", "c", 5.0)
    # g.addEdge("b", "d", 8.0)
    # g.addEdge("b", "e", 5.0)
    # g.addEdge("c", "d", 2.0)
    # g.addEdge("c", "g", 5.0)
    # g.addEdge("d", "h", 7.0)
    # g.addEdge("d", "g", 8.0)
    # g.addEdge("e", "f", 1.0)
    # g.addEdge("e", "g", 3.0)
    # g.addEdge("g", "h", 5.0)

    # graph 2 exercice 3.4
    # Ajouter les arêtes
    g.addEdge("a", "b", 4.0)
    g.addEdge("a", "c", 3.0)
    g.addEdge("b", "c", 5.0)
    g.addEdge("b", "f", 2.0)
    g.addEdge("c", "d", 2.0)
    g.addEdge("c", "f", 5.0)
    g.addEdge("d", "e", 4.0)
    g.addEdge("d", "f", 3.0)
    g.addEdge("e", "f", 3.0)

    # Obtenir un arbre couvrant de poids minimal du graphe et le poids minimal
    tree,cost = kruskal(g,computeMin=False)
    
    # S'il existe un tel arbre (i.e., si le graphe est connexe)
    if tree != None:
        
        # L'afficher
        print(tree,'\n',cost)
    
    else:
        print("Pas d'arbre couvrant")

# Applique l'algorithme de Kruskal pour trouver un arbre couvrant de poids minimal d'un graphe
# Retourne: Un arbre couvrant de poids minimal du graphe ou None s'il n'en existe pas
def kruskal(g,computeMin:bool = True):
    
    # Créer un nouveau graphe contenant les mêmes sommets que g
    tree = graph.Graph(g.nodes)
    
    # Nombre d'arêtes dans l'arbre
    addedEdges = 0
    cost = 0 # make the calcul of the cost of the whole tree

    # Récupérer toutes les arêtes de g
    edges = g.getEdges()
    
    # Trier les arêtes par poids croissant
    edges.sort(reverse=(not computeMin)) # if computeMin is deactivated, we find the tree with the maximum weight

    # try to detect a circle within the other edges. If not found, at the edge with the minimum weight to the tree.
    for i_edge in edges:
        cycle_detected = tree.createACycle(i_edge) #add the first node to the tree -> has the minimum weight then we start with him.
        if (cycle_detected == False):
            tree.addCopyOfEdge(i_edge)
            addedEdges = addedEdges + 1
            cost = cost + i_edge.weight

    return tree,cost




if __name__ == '__main__':
    main()
