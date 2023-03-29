import random
import numpy as np
import sys
import time

class Graph:
    def __init__(self, edges):
        self.adj_list = {}
        self.clusters = {}
        self.visited = {}
        for u, v in edges:
            self.add_edge(u, v)
            
    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
            self.clusters[u] = {u}
            self.visited[u] = False
        if v not in self.adj_list:
            self.adj_list[v] = []
            self.clusters[v] = {v}
            self.visited[v] = False
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
        
    def min_cut(self):
        while len(self.clusters) > 2:
            u, v = self.choose_random_edge() # choosing a random edge
            self.contract(u, v) # contract the randomly connected edge 
        min_cut = 0
        for i in self.adj_list: 
            #adj list only consists of connections to the other set
            #adding all the edges and dividing them by 2 will the number 
            #of edges connecting the 2 sets
            min_cut += len(self.adj_list[i])
        return min_cut // 2
        
    def choose_random_edge(self):
        u = random.choice(list(self.clusters.keys()))
        v = random.choice(self.adj_list[u])
        return u, v
        
    def contract(self, u, v):
        '''
        Merges two nodes into one node by updating the 
        cluster/ adj list and deleting the node from adj list/ cluster 
        '''
        self.clusters[u].update(self.clusters[v])
        del self.clusters[v]
        for i in self.adj_list[v]: #for each node in niebhourhood 
            if i != u: #extend the list when the nodes are not equal
                self.adj_list[u].append(i)
                self.adj_list[i].append(u)
            self.adj_list[i].remove(v)
        del self.adj_list[v] # deleting the merged node from adj list

    def count_components(self):
        """
        Returns the number of connected components
        Used to check if the graph has only one connected component
        """
        count = 0
        for u in self.adj_list:
            if not self.visited[u]:
                count += 1
                self.visited[u] = True
                stack = [u]
                while stack:
                    u = stack.pop()
                    for v in self.adj_list[u]:
                        if not self.visited[v]:
                            self.visited[v] = True
                            self.clusters[u].update(self.clusters[v])
                            stack.append(v)
            return count

    def format_print(self):
        for clno, cluster in enumerate(self.clusters.values()):
            for node in cluster:
                print("{} {}".format(node, clno + 1))


if __name__ == '__main__':
    #start = time.time()
    edges = np.loadtxt(sys.argv[1], dtype=int, delimiter = ' ')
    g = Graph(edges)
    #print("Graph generated: {}".format(time.time() - start))
    #print(g.count_components())
    min_cut = g.min_cut()
    #print("Min cut generated: {}".format(time.time() - start))
    print(min_cut)
    g.format_print()
    #print('Time taken: ', time.time() - start)