import numpy as np
import sys 
import time
import random

class DisjointSet:
    def __init__(self, graph):
        self.parent = {}
        self.rank = {}
        self.sets_count = len(graph)
        for node in graph.keys():
            self.parent[node] = node
            self.rank[node] = 0

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
     count = 0
     for node in range(len(uf)):
        if uf[node] not in set_list.keys():
            count +=1
            set_list[uf[node]] = count
        print("{} {}".format(node, set_list[uf[node]]))
            
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
    uf = DisjointSet(graph)
    nodes = list(graph.keys())
    while uf.sets_count > 2:
        if (uf.sets_count < 10000 == 0 and uf.sets_count % 1000==0) :
            print("Iteration index :", uf.sets_count)
        u = random.choice(nodes)
        if len(graph[u]) > 0: 
            v = graph[u].pop(random.randrange(len(graph[u])))
            graph[v].pop(graph[v].index(u))
            uf.union(u, v)
    cut_size = 0
    for u in nodes:
        for v in nodes:
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
