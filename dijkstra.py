import graph
import sys
import numpy as np

def main():
    cities = []
    cities.append("Paris")
    cities.append("Hambourg")
    cities.append("Londres")
    cities.append("Amsterdam")
    cities.append("Edimbourg")
    cities.append("Berlin")
    cities.append("Stockholm")
    cities.append("Rana")
    cities.append("Oslo")

    g = graph.Graph(cities)
    
    g.addArc("Paris", "Hambourg", 7)
    g.addArc("Paris",  "Londres", 4)
    g.addArc("Paris",  "Amsterdam", 3)
    g.addArc("Hambourg",  "Stockholm", 1)
    g.addArc("Hambourg",  "Berlin", 1)
    g.addArc("Londres",  "Edimbourg", 2)
    g.addArc("Amsterdam",  "Hambourg", 2)
    g.addArc("Amsterdam",  "Oslo", 8)
    g.addArc("Amsterdam", "Londres", 1)
    g.addArc("Stockholm",  "Oslo", 2)
    g.addArc("Stockholm",  "Rana", 5)
    g.addArc("Berlin",  "Amsterdam", 2)
    g.addArc("Berlin",  "Stockholm", 1)
    g.addArc("Berlin",  "Oslo", 3)
    g.addArc("Edimbourg",  "Oslo", 7)
    g.addArc("Edimbourg",  "Amsterdam", 3)
    g.addArc("Edimbourg",  "Rana", 6)
    g.addArc("Oslo",  "Rana", 2)
    
    # Applique l'algorithme de Dijkstra pour obtenir une arborescence
    pi,pred = dijkstra(g, "Paris")
    print('last state of pi = ',pi,'\n','Path from from value to index (exemple:from city 3(value) to city 2(index)  = ',pred)

def dijkstra(g, origin):
		
   # Get the index of the origin 
   r = g.indexOf(origin)
   all_arcs = g.getArcs() # get all arcs of the graph

   # Next node considered 
   pivot = r
   
   # Liste qui contiendra les sommets ayant été considérés comme pivot
   v2 = []
   # v2.append(pivot)

   
   pred = [0] * g.n
   
   # Les distances entre r et les autres sommets sont initialement infinies
   pi = [sys.float_info.max] * g.n
   pi[r] = 0

   # Ajouter votre code ici
   # look all the nodes of the graph
   # iter_dict = {}
   for j in range(1,g.n):

       if pivot not in v2:
           arcs_pivot = [x for x in all_arcs if x.id1==pivot] # selecting the nodes that have interface with the current pivot
           arcs_pivot.sort() #sort the distances between the nodes to find the minimal one
           for i_node in arcs_pivot:
               if (i_node.weight + pi[pivot]<=pi[i_node.id2]): # if the weight is less than the older one, we update it
                   if pi[i_node.id2] == sys.float_info.max:  # if the weight is still in infinite and the node is selectec, set the weight to 0
                       pi[i_node.id2] = 0
                   pi[i_node.id2] = i_node.weight + pi[pivot] # filling the pi table for the current pivot
                   pred[i_node.id2] = pivot
                   # if i_node.id2 != pivot:
                   #     pred[i_node.id2] = pivot

           v2.append(pivot) # append the older pivot
           aux=[]
           for i_v in range(0,g.n):
               if i_v not in v2:
                   aux.append(pi[i_v])
           pivot = pi.index(min(aux)) # update the pivot with the minimum value of pi

           i_i = 0
           while pivot in v2:  # pivot is a repeated number (as 6 for our first example)

               indexes = np.where(np.array(pi)==pi[pivot])
               aux2 = indexes[0].tolist().copy()
               pivot = aux2[i_i] # chooses the pivot that is not repeated
               i_i=i_i+1

   return pi,pred


   
if __name__ == '__main__':
    main()
