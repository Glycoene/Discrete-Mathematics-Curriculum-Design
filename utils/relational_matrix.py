def is_symmetric(matrix):
    length = len(matrix)

    for i in range(length):
        for j in range(i + 1, length):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

if __name__ == '__main__':
    matrix1 = [
        [1, 0, 0],
        [1, 1, 1],
        [1, 0, 0]
    ]
    matrix2 = [
        [1, 1, 0],
        [1, 1, 1],
        [0, 1, 1]
    ]
    print(is_symmetric(matrix1),is_symmetric(matrix2))
