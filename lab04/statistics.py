print("Статистика потока")
n = int(input("Введите количество чисел (n >= 1): "))
first_num = int(input("Введите число: "))
total_sum = first_num
max_value = first_num
positive_count = 0

if first_num > 0:
    positive_count += 1
for _ in range(n - 1):
    num = int(input("Введите число: "))
    total_sum += num
    if num > 0:
        positive_count += 1
    if num > max_value:
        max_value = num

print("----------")
print(f"Сумма: {total_sum}")
print(f"Положительных: {positive_count}")
print(f"Максимум: {max_value}")
print("----------")
