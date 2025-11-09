def is_symmetric(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1):  
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

matrix = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]

result = is_symmetric(matrix)
print(result)
