import numpy as np

def make_table(rows, columns):
    arr = np.arange(rows * columns).reshape(rows, columns)
    return arr.tolist()

def rectangle(matrix, row_start, row_stop, column_start, column_stop):
    arr = np.array(matrix)
    sliced = arr[row_start:row_stop, column_start:column_stop]
    return sliced.tolist()

def replace_rectangle(matrix, row_start, row_stop, column_start, column_stop, value):
    arr = np.array(matrix).copy()
    arr[row_start:row_stop, column_start:column_stop] = value
    return arr.tolist()

def matrix_vector_product(matrix, vector):
    mat = np.array(matrix)
    vec = np.array(vector)
    result = mat @ vec
    return result.tolist()

def matrix_multiply(left, right):
    l_arr = np.array(left)
    r_arr = np.array(right)
    result = l_arr @ r_arr
    return result.tolist()

def transpose_matrix(matrix):
    arr = np.array(matrix)
    return arr.T.tolist()

def solve_system(matrix, vector):
    mat = np.array(matrix)
    vec = np.array(vector)
    result = np.linalg.solve(mat, vec)
    return np.round(result, 6).tolist()

def tensor_channel_mean(tensor):
    arr = np.array(tensor)
    result = arr.mean(axis=-1)
    return result.tolist()

def point_distance(first, second):
    f = np.array(first)
    s = np.array(second)
    dist = np.linalg.norm(f - s)
    return float(np.round(dist, 6))
