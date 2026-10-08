print("Диапозон в обе стороны")
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

if a > b:
    print(a)
    while b != a:
      a = a - 1
      print(a)
    print("Готово")
else:
    print(a)
    while a != b:
      a = a + 1
      print(a)
    print("Готово")