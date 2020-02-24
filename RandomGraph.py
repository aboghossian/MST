import random
import math


# function to generate a random graph
# takes n (num nodes) and a dimension used for random weights
def generate_graph(n, dimensions):
    # n by n matrix of edges
    edge_list = [[0 for i in range(n)] for j in range(n)]

    # if dimensions = 0 just use random weights
    if dimensions == 0:
        for column in range(n):
            for row in range(column, n):
                if column == row:
                    edge_list[column][row] = 0
                else:
                    weight = random.uniform(0, 1)
                    edge_list[column][row] = weight
                    edge_list[row][column] = weight

    # otherwise generate n points in dimensions and have weights be distances
    if dimensions == 2:
        x = [random.uniform(0, 1) for v in range(n)]
        y = [random.uniform(0, 1) for v in range(n)]

        for column in range(n):
            for row in range(column, n):
                if column == row:
                    edge_list[column][row] = 0
                else:
                    weight = math.sqrt((x[column] - x[row])**2 + (y[column] - y[row])**2)
                    edge_list[column][row] = weight
                    edge_list[row][column] = weight

    if dimensions == 3:
        x = [random.uniform(0, 1) for v in range(n)]
        y = [random.uniform(0, 1) for v in range(n)]
        z = [random.uniform(0, 1) for v in range(n)]

        for column in range(n):
            for row in range(column, n):
                if column == row:
                    edge_list[column][row] = 0
                else:
                    weight = math.sqrt((x[column] - x[row]) ** 2 + (y[column] - y[row]) ** 2 + (z[column] - z[row])**2)
                    edge_list[column][row] = weight
                    edge_list[row][column] = weight

    if dimensions == 4:
        x = [random.uniform(0, 1) for v in range(n)]
        y = [random.uniform(0, 1) for v in range(n)]
        z = [random.uniform(0, 1) for v in range(n)]
        w = [random.uniform(0, 1) for v in range(n)]

        for column in range(n):
            for row in range(column, n):
                if column == row:
                    edge_list[column][row] = 0
                else:
                    weight = math.sqrt((x[column] - x[row])**2 + (y[column] - y[row])**2 + (z[column] - z[row])**2 + (w[column] - w[row])**2)
                    edge_list[column][row] = weight
                    edge_list[row][column] = weight

    return edge_list

