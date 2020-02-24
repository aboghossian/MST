import sys
from PrimsAlgoLL import *
from RandomGraph import *

# arguments passed by executable
mode = int(sys.argv[1])
numpoints = int(sys.argv[2])
numtrials = int(sys.argv[3])
dimension = int(sys.argv[4])

# seed random number generator for reproducibility
random.seed(1)

# array to store results
results = []

# run numtrials times
for i in range(numtrials):
    # generate graph
    g = generate_graph(numpoints, dimension)

    # calculate MST size
    mst_size = prims_ll(g, 0)

    # add to results
    results.append(mst_size)

# print average MST size
print(sum(results)/numtrials)
