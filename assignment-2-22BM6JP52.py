import random
import numpy as np
import sys
import time

class Graph:
    def __init__(self, edges):
        self.adj_list = {}
        self.clusters = {}
        for u, v in edges:
            self.add_edge(u, v)
            
    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
            self.clusters[u] = {u}
        if v not in self.adj_list:
            self.adj_list[v] = []
            self.clusters[v] = {v}
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
        
    def min_cut(self):
        while len(self.clusters) > 2:
            u, v = self.choose_random_edge()
            self.contract(u, v)
        min_cut = 0
        for i in self.adj_list:
            min_cut += len(self.adj_list[i])
        return min_cut // 2, list(self.clusters.values())
        
    def choose_random_edge(self):
        u = random.choice(list(self.clusters.keys()))
        v = random.choice(self.adj_list[u])
        return u, v
        
    def contract(self, u, v):
        # merge v into u
        self.clusters[u].update(self.clusters[v])
        del self.clusters[v]
        for i in self.adj_list[v]:
            if i != u:
                self.adj_list[u].append(i)
                self.adj_list[i].append(u)
            self.adj_list[i].remove(v)
        del self.adj_list[v]

if __name__ == '__main__':
    start = time.time()
    edges = np.loadtxt(sys.argv[1], dtype=int, delimiter = ' ')
    g = Graph(edges)
    min_cut, clusters = g.min_cut()
    print('The minimum cut is:', min_cut)
    print('The clusters are:', clusters)
    print('Time taken: ', time.time() - start)