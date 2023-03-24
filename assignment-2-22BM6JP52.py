import numpy as np
import sys 
import time
import random

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.sets_count = n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        self.sets_count -= 1
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1

def format_print(uf):
     set_list = {}
     count = 1
     for node, set_id in uf.items():
        if set_id not in set_list:
            count +=1
            set_list[set_id] = count
        print("{} {}".format(node, set_list[set_id]))
            

		
def gen_graph(edges):
	graph = {}
	for edge in edges:
		if edge[0] not in graph:
			graph[edge[0]] = []
		if edge[1] not in graph:
			graph[edge[1]] = []
		graph[edge[0]].append(edge[1])
		graph[edge[1]].append(edge[0])
	return graph
    
def karger_min_cut(graph):
    n = len(graph)
    uf = DisjointSet(n)
    while uf.sets_count > 2:
        u = random.randint(0, n-1)
        v = random.choice(graph[u])
        uf.union(u, v)
    cut_size = 0
    for u in range(n):
        for v in graph[u]:
            if uf.find(u) != uf.find(v):
                cut_size += 1
    return cut_size // 2, uf

if __name__ == "__main__":

	if(len(sys.argv) != 2):
		exit("Number of arg didn't match")

	start = time.time()
	edges = np.loadtxt(sys.argv[1], dtype=int, delimiter = ' ')
	graph = gen_graph(edges)
	min_cut, nf = karger_min_cut(graph)
	print(min_cut)
	format_print(nf.parent)
	print("Total time: {}".format(time.time() - start))
