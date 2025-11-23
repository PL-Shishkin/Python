def is_symmetric(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

# Чтение матрицы из файла
with open('Шишкин_Ярослав_уб-52_vvod.txt', 'r') as f:
    matrix = []
    for line in f:
        row = [int(x) for x in line.split()]
        matrix.append(row)

# Проверка симметричности
result = is_symmetric(matrix)

# Запись результата в файл
with open('Шишкин_Ярослав_уб-52_vivod.txt', 'w') as f:
    f.write(str(result))
