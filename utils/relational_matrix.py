import numpy

def is_symmetric(matrix):
    rows, cols = matrix.shape
    if rows != cols:
        return False
    for i in range(rows):
        for j in range(i + 1, cols):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

if __name__ == '__main__':
    matrix1 = numpy.array([
        [1, 0, 0],
        [1, 1, 1],
        [1, 0, 0]
    ])
    matrix2 = numpy.array([
        [1, 1, 0],
        [1, 1, 1],
        [0, 1, 1]
    ])
    print(is_symmetric(matrix1),is_symmetric(matrix2))
