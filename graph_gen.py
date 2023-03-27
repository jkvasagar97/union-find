

import random

def generate_edges(num_vertices):
    edges = []
    for i in range(num_vertices):
        for j in range(i+1, num_vertices):
            edges.append((i, j))
    random.shuffle(edges)
    return edges

def generate_connected_edges(num_vertices):
    edges = []
    remaining_vertices = set(range(num_vertices))
    visited_vertices = set()
    start_vertex = random.choice(list(remaining_vertices))
    visited_vertices.add(start_vertex)
    remaining_vertices.remove(start_vertex)
    while remaining_vertices:
        u = random.choice(list(visited_vertices))
        v = random.choice(list(remaining_vertices))
        edges.append((u, v))
        visited_vertices.add(v)
        remaining_vertices.remove(v)
    random.shuffle(edges)
    return edges

if __name__ == '__main__':

    edges = generate_connected_edges(10000)
    file = open('items.txt','w')
    for item in edges:
	    file.write("{} {}\n".format(item[0], item[1]))
    file.close()