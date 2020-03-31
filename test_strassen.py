from strassen import *
from datetime import datetime
import sys
from random import randint

start = int(sys.argv[1])
end = int(sys.argv[2])

a = [[randint(-1, 1) for j in range(end)] for i in range(end + 1)]
b = [[randint(-1, 1) for j in range(end)] for i in range(end + 1)]

print("starting")
splits = [ceil(end/2**i) for i in range(1, floor(log2(end)))]
print(splits)
for c in splits:

    t_start = datetime.now()
    strassens(a, b, crossover = c)
    t = datetime.now() - t_start

    print(c, t)
