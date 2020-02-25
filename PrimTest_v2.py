from PrimsAlgoLL_v2 import *
from RandomGraphLL import *
import random


out_file = open("results.txt", "w")
trials = 5
num_points = [128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144]
dims = [0, 2, 3, 4]

random.seed(1)

for n in num_points:
    for d in dims:
        res = 0
        for t in range(trials):
            g = generate_graph_ll(n, d)
            mst = prims_ll_v2(g, 0)
            res += mst
            print(t)
        res = res/trials
        line = "{}, {}, {}".format(d, n, res)
        out_file.write(line + "\n")
        out_file.flush()
        print(n, d, res)
out_file.close()
