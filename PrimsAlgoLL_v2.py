from LinkedList import *


# function to perform Prim's algorithm to calculate size of MST
# takes graph and a vertex to start from
def prims_ll_v2(graph, s):

    n = range(len(graph))
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
        adj_list = graph[v]
        current = adj_list.head
        while current is not None:
            w = current.vertex
            e = current.weight
            if (distances[w] > e) and (w not in vertex_set):
                distances[w] = e
                in_heap = heap.search(w)
                if in_heap is not None:
                    in_heap.weight = distances[w]
                else:
                    heap.add(Node(w, distances[w]))
            current = current.next

    # return the sum of the distance array (MST edges)
    print(len(vertex_set) == len(graph))
    return sum(distances)
