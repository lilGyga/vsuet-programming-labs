print("Замена отрицательных чисел их модулями")
numbers = []
for part in input("Введите целые числа через пробел: ").split():
    numbers.append(int(part))

transformed = []
for num in numbers:
    transformed.append(abs(num))

print("----------")
print(f"Исходный список: {numbers}")
print(f"Новый список: {transformed}")
print("----------")