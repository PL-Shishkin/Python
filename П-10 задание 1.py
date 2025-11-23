def is_symmetric(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True


with open('Шишкин_Ярослав_уб-52_vvod.txt', 'r') as f:
    matrix = []
    for line in f:
        row = [int(x) for x in line.split()]
        matrix.append(row)

result = is_symmetric(matrix)

with open('Шишкин_Ярослав_уб-52_vivod.txt', 'w') as f:
    f.write(str(result))
