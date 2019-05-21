from graph import *

def prim_algorithm(graph):

    """
    A greedy algorithm that finds a minimum spanning tree (MST) for a weighted undirected graph.
    https://en.wikipedia.org/wiki/Prim%27s_algorithm
    """

    # initialization

    weights = {}
    parents = {}
    status  = {}

    for index in graph.graph:

        weights[index] = INFINITY
        parents[index] = -1
        status[index]  = NOT_VIDISTED
    
    # get the first index of MST

    start = next(iter(graph.graph))
    weights[start] = 0
    
    while True:

        min_v = INFINITY
        current_index = None

        for index in graph.graph:

            if min_v > weights[index] and status[index] != FINISHED:
                
                current_index = index
                min_v         = weights[index]

        if not current_index:
            
            # finish
            break

        status[current_index] = FINISHED

        for adjacent_edge in graph.graph[current_index]:

            if status[adjacent_edge.end] == FINISHED or adjacent_edge.w == INFINITY:
                
                continue
            
            if weights[adjacent_edge.end] > adjacent_edge.w:

                weights[adjacent_edge.end] = adjacent_edge.w
                parents[adjacent_edge.end] = current_index
                status[adjacent_edge.end]  = VISITED

    sum_v = 0
    connections = []

    for index in graph.graph:

        if parents[index] == -1:
            
            continue

        for adjacent_edge in graph.graph[index]:
            
            if adjacent_edge.end == parents[index]:

                sum_v += adjacent_edge.w
                connections.append(adjacent_edge)
                break
    
    return connections, sum_v

if __name__ == '__main__':

    graph = Graph()

    connections = [(1, 2), (1, 3), (2, 3), (2, 4), (3, 5), (4, 6), (5, 6)]

    for c in connections:
        
        i, j, w = c[0], c[1], 1

        graph.add_edge(i, j, w)
        graph.add_edge(j, i, w)

    connections, sum_v = prim_algorithm(graph)
    
    print('Total length: %d' % sum_v)

    for c in connections:
        print(c)