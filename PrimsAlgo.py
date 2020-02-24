# function to perform Prim's algorithm to calculate size of MST
# takes graph and a vertex to start from


def prims(graph, s):

    vertex_set = []  # visited vertices
    heap = [s]  # vertex names in the heap
    heap_values = [0]  # vertex values in the heap

    distances = [100] * len(graph)  # distance array
    previous = [None] * len(graph)  # previous array

    distances[s] = 0  # set start distance to 0

    # while there are still elements in the heap
    while len(heap_values) > 0:
        i = heap_values.index(min(heap_values))  # get index of the minimum weighted edge
        v = heap[i]  # find the vertex associated

        # delete that vertex from heap arrays
        del(heap[i])
        del(heap_values[i])

        vertex_set.append(v)  # mark as visited

        # loop through neighbors updating distances if not visited
        for w in range(len(graph[v])):
            if (w not in vertex_set) and (distances[w] > graph[v][w]):
                distances[w] = graph[v][w]
                previous[w] = v
                if w in heap:
                    i = heap.index(w)
                    heap_values[i] = distances[w]
                else:
                    heap.append(w)
                    heap_values.append(distances[w])

    # return the sum of the distance array (MST edges)
    return sum(distances)
