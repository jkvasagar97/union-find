import numpy as np
import sys 
import time


class DisjointSet:
	def __init__(self, n):
		self.rank = [1] * n
		self.parent = [i for i in range(n)]
		self.sets_count = n

	def find(self, x):
		if (self.parent[x] != x):
			self.parent[x] = self.find(self.parent[x])
		return self.parent[x]

	def union(self, x, y):
		xset = self.find(x)
		yset = self.find(y)

		if xset == yset:
			return

		else:
			self.parent[yset] = xset
			self.rank[xset] = self.rank[xset] + 1	
			self.sets_count = self.sets_count - 1 
		

if __name__ == "__main__":

	if(len(sys.argv) != 2):
		exit("Number of arg didn't match")

	start = time.time()
	print(start)
	edges = np.loadtxt(sys.argv[1], dtype=int, delimiter = ' ')
	graph = DisjointSet(edges.max()+1)
	while (graph.sets_count > 3):
		edge_index = np.random.choice(edges.shape[0], replace=False)
		random_edge = edges[edge_index,:]
		graph.union(random_edge[0], random_edge[1])
		if(graph.sets_count%1000 == 0):
			print('Number of sets = {}: {}'.format(graph.sets_count, time.time() - start))
	print(time.time() - start)
	print(graph.parent)
