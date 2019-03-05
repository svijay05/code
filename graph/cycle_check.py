

"""
Given a directed graph G=(V,E), find whether G has a cycle.


Core logic is back edge detection; that is an edge from a node to itself or 
to its ancestor

"""

from collections import defaultdict


class Graph():

    def __init__(self):
        # if a key is not present.. creates it with the value as empty list
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, visited, start_vertex,recur_stack):
        print(recur_stack)
        if visited[start_vertex] == False and start_vertex not in recur_stack:
            visited[start_vertex] = True
            #print(start_vertex, end=" ")
            for neighbour in self.graph[start_vertex]:
                recur_stack.append(start_vertex)
                self.dfs(visited, neighbour,recur_stack)
        else:
            return  False

    def is_cycle_present(self, start_vertex):
        visited = [False]*len(self.graph)
        recur_stack = []
        return self.dfs(visited, start_vertex,recur_stack)


if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print(g.__dict__)

    is_cycle_present = g.is_cycle_present(0)
    print(is_cycle_present)
