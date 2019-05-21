from graph import *
from queue import Queue

class BFSGraph(Graph):

    """
    The algorithm starts at the tree root (or some arbitrary node of a graph, sometimes referred to as a 'search key'), and explores all of the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level.
    https://en.wikipedia.org/wiki/Breadth-first_search
    """

    def __init__(self):

        Graph.__init__(self)

    def bfs(self, start):

        t = 0
        distance = {}

        for index in self.graph:

            distance[index] = INFINITY
        
        distance[start] = 0

        queue = Queue()
        queue.enqueue(start)

        while not queue.is_empty:

            index = queue.dequeue()

            adjacents = self.graph[index]

            for adjacent_edge in adjacents:

                adjacent_index = adjacent_edge.end

                if distance[adjacent_index] != INFINITY:
                    
                    continue

                distance[adjacent_index] = distance[index] + 1
                queue.enqueue(adjacent_index)

        return distance

if __name__ == '__main__':

    graph = BFSGraph()

    connections = [(1, 2), (1, 3), (2, 3), (2, 4), (3, 5), (4, 6), (5, 6)]

    for c in connections:
        
        i, j = c[0], c[1]

        graph.add_edge(i, j)
        graph.add_edge(j, i)

    distance = graph.bfs(1)

    print('visited: ' + ' '.join(str(distance[index]) if distance[i] != INFINITY else 'N' for index in distance))