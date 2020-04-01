from strassen import *
from random import uniform


def generate_graph(p):
    p = 1-p
    g = [[1 if uniform(0, 1) >= p else 0 for j in range(1024)] for i in range(1024)]
    return g


outfile = open("results.csv", "w")
for p in [0.01, 0.02, 0.03, 0.04, 0.05]:
    for t in range(5):
        g = generate_graph(p)
        a2 = strassens(g, g, crossover=128)
        a3 = strassens(g, a2, crossover=128)
        triangles = sum([a3[i][i] for i in range(len(a3))])/6

        line = "{},{}".format(p, triangles)
        outfile.write(line + "\n")
        outfile.flush()
        print(p, triangles)
outfile.close()
