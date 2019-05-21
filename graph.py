NOT_VIDISTED = 0
VISITED      = 1
FINISHED     = 2

INFINITY     = 999999999

class Edge(object):

    def __init__(self, start, end, w=0):

        self.start = start
        self.end   = end
        self.w     = w
    
    def __contains__(self, v):
        
        if isinstance(v, int):
            return self.v == v

        if isinstance(v, Edge):
            return self == v

        raise ValueError('Edge can be evaluated only with integer or edge class')

    def __str__(self):

        return '(start: %d, end: %d, weight: %.2f)' % (self.start, self.end, self.w)

    def __repr__(self):

        return str(self)

    @staticmethod
    def contain(edges, end):

        for e in edges:

            if e.end == end:

                return True

        return False


class Graph(object):

    """
    A simple graph
    https://en.wikipedia.org/wiki/Graph_theory
    """

    def __init__(self):

        self.graph = {}

    def add_edge(self, i, j, w=0):

        if not i in self.graph:
            self.graph[i] = []

        edge = Edge(i, j, w)
        self.graph[i].append(edge)
    
    def edge_of(self, i, j):

        for edge in self.graph[i]:

            if edge.end == j:
                
                return edge
        
        return None
    
    def __str__(self):

        items = {}
        i = 0
        for index in self.graph:

            items[i] = index
            i += 1

        matrix = []

        for i in items:

            row_index = items[i]

            row_vals = []

            for j in items:

                column_index = items[j]
                
                if Edge.contain(self.graph[row_index], column_index):
                    
                    v = '1'

                else:

                    v = '0'
                
                row_vals.append(v)
            
            matrix.append(' '.join(row_vals))
        
        return '\n'.join(matrix)


if __name__ == '__main__':

    graph = Graph()

    connections = [(1, 2), (1, 3), (2, 3), (2, 4), (3, 5), (4, 6), (5, 6)]

    for c in connections:
        
        i, j = c[0], c[1]

        graph.add_edge(i, j)
        graph.add_edge(j, i)
    
    print(graph)
