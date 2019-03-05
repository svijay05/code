

"""
DFS

BFS uses a queue,meanwhile DFS uses stack


Applications:

1. Topological sorting
every directed edge uv, vertex u comes before v in the ordering. 
Topological Sorting for a graph is not possible if the graph is not a DAG.

2. cycle checking
3. biparite testing
    A Bipartite Graph is a graph whose vertices can be divided into two independent sets, U and V
    such that every edge (u, v) either connects a vertex from U to V or a vertex from V to U.
4. solving maze problems



Time complexity O(V+E)

Space complexity O(V)

"""

from collections import defaultdict


class Graph():

    def __init__(self):
        # if a key is not present.. creates it with the value as empty list
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, visited,start_vertex):

        if visited[start_vertex] == False:

            visited[start_vertex] = True
            print(start_vertex, end=" ")
            neighbours = self.graph[start_vertex]

            for n in neighbours:
                self.dfs(visited, n)

    def dfs_util(self, start_vertex):
        visited = [False] * len(self.graph)
        self.dfs(visited,start_vertex)


if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print(g.__dict__)
    g.dfs_util(0)
    print()
