def add_matrices(a, b):
    n = len(a)
    out_mat = [[a[i][j] + b[i][j] for j in range(n)] for i in range(n)]
    return out_mat

def subtract_matrices(a, b):
    n = len(a)
    out_mat = [[a[i][j] - b[i][j] for j in range(n)] for i in range(n)]
    return out_mat

def multiply_matrices(a, b):
    out_mat = [[0 for i in range(len(b[0]))] for j in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                out_mat[i][j] += a[i][k] * b[k][j]
    return out_mat
