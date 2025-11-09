from math import pi

print("Выберите фигуру:\n"
      "1. Квадрат\n"
      "2. Прямоугольник\n"
      "3. Круг\n"
      "4. Треугольник")
choice = input("Ваша фигура: ")

if choice == '1':
    a = float(input("Длина стороны квадрата: "))
    print(a**2)
elif choice == '2':
    w = float(input("Ширина прямоугольника: "))
    h = float(input("Высота прямоугольника: "))
    print(w*h)
elif choice == '3':
    r = float(input("Радиус круга: "))
    print(pi*r**2)
elif choice == '4':
    b = float(input("Основание треугольника: "))
    h = float(input("Высота треугольника: "))
    print((b*h)/2)
else:
    print("Ошибка выбора!")
