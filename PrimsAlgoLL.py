from LinkedList import *


# function to perform Prim's algorithm to calculate size of MST
# takes graph and a vertex to start from
def prims_ll(graph, s):

    vertex_set = []  # visited vertices
    heap = LinkedList()  # heap
    heap.add(Node(s, 0))  # add s with weight 0

    distances = [100] * len(graph)  # distance array

    distances[s] = 0  # set start distance to 0

    # while there are still elements in the heap
    while not heap.is_empty():
        v = heap.delete_min()  # get index of the minimum weighted edge
        vertex_set.append(v)  # mark as visited

        # loop through neighbors updating distances if not visited
        for w in range(len(graph[v])):
            if (w not in vertex_set) and (distances[w] > graph[v][w]):
                distances[w] = graph[v][w]
                in_heap = heap.search(w)
                if in_heap is not None:
                    in_heap.weight = distances[w]
                else:
                    heap.add(Node(w, distances[w]))

    # return the sum of the distance array (MST edges)
    return sum(distances)
