print("Анализ нечетных чисел")
n = int(input("Введите количество чисел (n >= 0): "))
odd_count = 0
odd_sum = 0

for _ in range(n):
    num = int(input("Введите число: "))
    if num % 2 != 0:
        odd_count += 1
        odd_sum += num

print("----------")
print(f"Количество: {odd_count}")
print(f"Сумма: {odd_sum}")
print("----------")
