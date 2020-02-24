from PrimsAlgo import *
from RandomGraph import *
import random


out_file = open("results.txt", "w")
trials = 5
num_points = [128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144]
dims = [0, 2, 3, 4]

for n in num_points:
    for d in dims:
        random.seed(d * n)
        res = 0
        for t in range(trials):
            g = generate_graph(n, d)
            mst = prims(g, 0)
            res += mst
        res = res/trials
        line = "{}, {}, {}".format(d, n, res)
        out_file.write(line + "\n")
        print(n, d)
out_file.close()
