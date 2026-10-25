print("Отбор нечётных чисел")
numbers = []
for part in input("Введите целые числа через пробел: ").split():
    numbers.append(int(part))

selected = []
for num in numbers:
    if num % 2 != 0:
        selected.append(num)

sorted_selected = sorted(selected)

print("----------")
print(f"Выборка: {selected}")
print(f"Количество: {len(selected)}")
print(f"Сумма: {sum(selected)}")
print(f"Отсортированная копия: {sorted_selected}")
print("----------")