from graph import *

class DFSGraph(Graph):

    """
    The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of a graph) and explores as far as possible along each branch before backtracking.
    https://en.wikipedia.org/wiki/Depth-first_search
    """

    def __init__(self):

        Graph.__init__(self)
    
    def dfs(self, start):

        self.t      = 0
        self.status = {}
        self.visited_order  = {}
        self.finished_order = {}

        for index in self.graph:

            self.status[index]         = NOT_VIDISTED
            self.visited_order[index]  = None
            self.finished_order[index] = None

        # first try
        self.__dfs_visit(start)   

        for index in self.graph:

            if self.status[index] == NOT_VIDISTED:

                self.__dfs_visit(index)   

        return self.visited_order, self.finished_order   

    def __dfs_visit(self, index):

        self.t += 1
        
        self.status[index] = VISITED
        self.visited_order[index] = self.t

        adjacents = self.graph[index]

        for adjacent_edge in adjacents:

            adjacent_index = adjacent_edge.end

            if self.status[adjacent_index] == NOT_VIDISTED:

                self.__dfs_visit(adjacent_index)

        self.t += 1

        self.status[index] = FINISHED
        self.finished_order[index] = self.t

if __name__ == '__main__':

    graph = DFSGraph()

    connections = [(1, 2), (1, 3), (2, 3), (2, 4), (3, 5), (4, 6), (5, 6)]

    for c in connections:
        
        i, j = c[0], c[1]

        graph.add_edge(i, j)
        graph.add_edge(j, i)

    # depth first search
    visited_order, finished_order = graph.dfs(1)
    
    print('visited: ' + ' '.join(str(visited_order[i]) if visited_order[i] != INFINITY else 'N' for i in visited_order))
    print('finished: ' + ' '.join(str(finished_order[i]) if finished_order[i] != INFINITY else 'N' for i in finished_order))
