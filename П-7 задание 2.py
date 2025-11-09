arrays = [
    [1, 2, 3, 4, 5],
    [-1, 0, 1, 2, 3],
    [10, 20, 30]
]

for i, arr in enumerate(arrays):
    total_sum = sum(arr)
    average = total_sum / len(arr)  
    print(f"Массив {i+1}: Сумма = {total_sum}, Среднеарифметическое = {average:.2f}")
