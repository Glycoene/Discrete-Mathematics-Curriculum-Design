def is_symmetric(matrix):
    length = len(matrix)
    for i in range(length):
        for j in range(i + 1, length):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

if __name__ == '__main__':
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    matrix2 = [
        [1, 2, 3],
        [2, 1, 4],
        [3, 4, 1]
    ]
    print(is_symmetric(matrix1))
    print(is_symmetric(matrix2))