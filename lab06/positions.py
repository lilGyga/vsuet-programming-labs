print("Поиск позиций максимального элемента")
numbers = []
for part in input("Введите целые числа через пробел: ").split():
    numbers.append(int(part))

print("----------")
if len(numbers) == 0:
    print("Нет данных")
else:
    max_val = max(numbers)
    positions = []
    for index, num in enumerate(numbers):
        if num == max_val:
            positions.append(index)
    print(f"Индексы максимума: {positions}")
print("----------")