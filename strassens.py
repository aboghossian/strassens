from matrix_operations import *
from math import ceil, floor, log2


def strassens(a, b, crossover=2):
    n = length(a)

    # base case
    if n <= crossover:
        result = multiply_matrices(a, b)

    # recursive case
    else:
        # if not a power of 2
        if ceil(log2(n)) != floor(log2(n)):
            # pad with zeroes
            new_n = 2 ** ceil(log2(n))
            break
        else:
            new_n = n

        # where to split the matrix
        split = new_n//2

        # define sub-matrices
        A = [[a[i][j] for j in range(0, split)] for i in range(0, split)]
        B = [[a[i][j] for j in range(split, new_n)] for i in range(0, split)]
        C = [[a[i][j] for j in range(0, split)] for i in range(split, new_n)]
        D = [[a[i][j] for j in range(split, new_n)] for i in range(split, new_n)]
        E = [[b[i][j] for j in range(0, split)] for i in range(0, split)]
        F = [[b[i][j] for j in range(split, new_n)] for i in range(0, split)]
        G = [[b[i][j] for j in range(0, split)] for i in range(split, new_n)]
        H = [[b[i][j] for j in range(split, new_n)] for i in range(split, new_n)]

        # sub-multiplications
        P1 = strassens(A, subtract_matrices(F, H))
        P2 = strassens(add_matrices(A, B), H)
        P3 = strassens(add_matrices(C, D), E)
        P4 = strassens(D, subtract_matrices(G, E))
        P5 = strassens(add_matrices(A, D), add_matrices(E, H))
        P6 = strassens(subtract_matrices(B, D), add_matrices(G, H))
        P7 = strassens(subtract_matrices(A, C), add_matrices(E, F))

        # combine results
        R1 = add_matrices(subtract_matrices(add_matrices(P5, P4), P2), P6)
        R2 = add_matrices(P1, P2)
        R3 = add_matrices(P3, P4)
        R4 = add_matrices(subtract_matrices(add_matrices(P5, P1), P3), P7)

        result = [R1 + R2, R3 + R4]

    return result
