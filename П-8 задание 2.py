def move_max_to_top_left(matrix):
    max_value = float('-inf')  
    max_pos = (-1, -1)  
    
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] > max_value:
                max_value = matrix[i][j]
                max_pos = (i, j)

    matrix[max_pos[0]], matrix[0] = matrix[0], matrix[max_pos[0]]
    
    for k in range(len(matrix)):
        matrix[k][max_pos[1]], matrix[k][0] = matrix[k][0], matrix[k][max_pos[1]]


matrix = [
    [3, 1, 4],
    [2, 5, 6],
    [9, 8, 7]
]

move_max_to_top_left(matrix)

for row in matrix:
    print(row)
