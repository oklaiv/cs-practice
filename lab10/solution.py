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

