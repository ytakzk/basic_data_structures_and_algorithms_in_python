import heapq # use built-in library

# Note: Our pop method returns the smallest item, not the largest (called a “min heap” in textbooks;
# a “max heap” is more common in texts because of its suitability for in-place sorting).
# https://docs.python.org/3.7/library/heapq.html

NOT_VIDISTED = 0
VISITED      = 1
FINISHED     = 2

INFINITY     = 999999999

def dijikstra_algorithm(edges, start):

    """
    An algorithm for finding the shortest paths between nodes in a graph with a priority queue.
    https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
    """

    # initialization

    queue = [] # The list of a tuple of (distance, index).

    distances = {}
    status    = {}

    for index in edges:

        distances[index] = INFINITY
        status[index]    = NOT_VIDISTED

    # get the first index of MST

    distances[start] = 0
    status[start]    = VISITED
    heapq.heappush(queue, (0, start))

    while len(queue) > 0:

        distance, current_index = heapq.heappop(queue)
        status[current_index] = FINISHED

        if distances[current_index] < distance:

            continue

        for adjacent_index, adjacent_weight in edges[current_index]:
            
            if status[adjacent_index] == FINISHED:
                
                continue

            if distances[adjacent_index] > distances[current_index] + adjacent_weight:
                
                distances[adjacent_index] = distances[current_index] + adjacent_weight

                heapq.heappush(queue, (distances[adjacent_index], adjacent_index))
                status[adjacent_index] = VISITED

    return distances

if __name__ == '__main__':

    edges = {}

    connections = [(1, 2, 1), (1, 3, 10), (2, 3, 1), (2, 4, 2), (3, 5, 2), (4, 6, 5), (5, 6, 3)]

    for c in connections:
        
        i, j, w = c[0], c[1], c[2]

        if not i in edges:

            edges[i] = []

        if not j in edges:

            edges[j] = []
        
        # express an edge as a tuple of (its adjacent index, its weight)
        edges[i].append((j, w))
        edges[j].append((i, w))

    distances = dijikstra_algorithm(edges=edges, start=1)

    for index in distances:

        print('node: %d, distance: %d' % (index, distances[index]))




 