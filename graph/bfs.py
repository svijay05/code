

"""
BFS

BFS uses a queue,meanwhile DFS uses stack


Applications:
1. Shortest Path and Minimum Spanning Tree for unweighted graph
2. cycle checking
3. biparite testing
    A Bipartite Graph is a graph whose vertices can be divided into two independent sets, U and V
    such that every edge (u, v) either connects a vertex from U to V or a vertex from V to U.
4. social networking websites


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

    def bfs(self, start_vertex):

        visited = [False] * len(self.graph)
        queue = []

        # mark it visited and enqueue it
        visited[start_vertex] = True
        queue.append(start_vertex)

        while queue:
            
            # deque it and print 
            vertex = queue.pop(0)
            print(vertex,end="->")

            # add neighbouring unvisited vetex to queue

            for neighbour in self.graph[vertex]:
                if visited[neighbour] != True:
                    visited[neighbour] = True
                    queue.append(neighbour)

                    



if __name__ == "__main__":
    g=Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print(g.__dict__)

    g.bfs(2)
