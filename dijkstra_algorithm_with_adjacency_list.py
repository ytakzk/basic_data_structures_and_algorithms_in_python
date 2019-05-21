from graph import *

def dijikstra_algorithm(graph, start):

    """
    An algorithm for finding the shortest paths between nodes in a graph with an adjacency list.
    https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
    """

    # initialization

    distances = {}
    status    = {}

    for index in graph.graph:

        distances[index] = INFINITY
        status[index]    = NOT_VIDISTED

    # get the first index of MST

    distances[start] = 0
    
    while True:

        min_v = INFINITY
        current_index = None

        for index in graph.graph:

            if min_v > distances[index] and status[index] != FINISHED:
                
                current_index = index
                min_v         = distances[index]

        if not current_index:
            
            # finish
            break

        status[current_index] = FINISHED

        for adjacent_edge in graph.graph[current_index]:

            if status[adjacent_edge.end] == FINISHED or adjacent_edge.w == INFINITY:
                
                continue
            
            if distances[adjacent_edge.end] > distances[current_index] + adjacent_edge.w:

                distances[adjacent_edge.end] = distances[current_index] + adjacent_edge.w
                status[adjacent_edge.end]    = VISITED

    return distances


if __name__ == '__main__':

    graph = Graph()

    connections = [(1, 2, 1), (1, 3, 10), (2, 3, 1), (2, 4, 2), (3, 5, 2), (4, 6, 5), (5, 6, 3)]

    for c in connections:
        
        i, j, w = c[0], c[1], c[2]
        
        graph.add_edge(i, j, w)
        graph.add_edge(j, i, w)

    distances = dijikstra_algorithm(graph, 1)
    
    for index in distances:

        print('node: %d, distance: %d' % (index, distances[index]))