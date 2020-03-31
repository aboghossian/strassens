from math import ceil, floor
from random import randint
import sys


def add_matrices(a, b):
    return [[x + y for x, y in zip(col_a, col_b)] for col_a, col_b in zip(a, b)]


def subtract_matrices(a, b):
    return [[x - y for x, y in zip(col_a, col_b)] for col_a, col_b in zip(a, b)]


def multiply_matrices(a, b):
    z_b = list(zip(*b))
    return [[sum(x * y for x, y in zip(a_row, b_col)) for b_col in z_b] for a_row in a]


def read_file(filename, d):
    dims = range(d)
    a = [[0 for i in dims] for j in dims]
    b = [[0 for i in dims] for j in dims]
    with open(filename) as f:
        i = 0
        j = 0
        for line in f:
            if i < d:
                a[i][j] = int(line.strip())
                j += 1
                if j > d-1:
                    j = 0
                    i += 1
            else:
                b[i-d][j] = int(line.strip())
                j += 1
                if j > d-1:
                    j = 0
                    i += 1
    return a, b


def strassens(a, b, crossover=2):
    n = len(a)

    # base case
    if n <= crossover:
        return multiply_matrices(a, b)

    # recursive case
    else:
        range_n = range(n)
        # if not a power of 2
        if n%2 != 0:
            # find next power of 2
            new_n = n + 1

            # pad with zeroes
            a = [a[i] + [0] for i in range_n] + [[0] * new_n]
            b = [b[i] + [0] for i in range_n] + [[0] * new_n]

        else:
            new_n = n

        # where to split the matrix
        split = new_n//2
        first_half = range(0, split)
        second_half = range(split, new_n)

        # define sub-matrices
        A = [a[i][:split] for i in first_half]
        B = [a[i][split:new_n] for i in first_half]
        C = [a[i][:split] for i in second_half]
        D = [a[i][split:new_n] for i in second_half]
        E = [b[i][:split] for i in first_half]
        F = [b[i][split:new_n] for i in first_half]
        G = [b[i][:split] for i in second_half]
        H = [b[i][split:new_n] for i in second_half]

        # sub-multiplications
        P1 = strassens(A, subtract_matrices(F, H), crossover=crossover)
        P2 = strassens(add_matrices(A, B), H, crossover=crossover)
        P3 = strassens(add_matrices(C, D), E, crossover=crossover)
        P4 = strassens(D, subtract_matrices(G, E), crossover=crossover)
        P5 = strassens(add_matrices(A, D), add_matrices(E, H), crossover=crossover)
        P6 = strassens(subtract_matrices(B, D), add_matrices(G, H), crossover=crossover)
        P7 = strassens(subtract_matrices(A, C), add_matrices(E, F), crossover=crossover)

        # combine results
        result = list(map(lambda x,y:x+y, add_matrices(subtract_matrices(add_matrices(P5, P4), P2), P6), add_matrices(P1, P2)))
        result.extend(list(map(lambda x,y:x+y, add_matrices(P3, P4), subtract_matrices(subtract_matrices(add_matrices(P5, P1), P3), P7))))
        return [result[i][:n]for i in range_n]


if __name__ == "__main__":
    flag = int(sys.argv[1])
    dimension = int(sys.argv[2])
    filename = sys.argv[3]

    a, b = read_file(filename, dimension)

    product = strassens(a, b, crossover=128)

    for i in range(dimension):
        print(product[i][i])
