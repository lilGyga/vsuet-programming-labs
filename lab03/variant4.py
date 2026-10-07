print("Результат теста")
score = int(input("Введите результат теста (0-100): "))

if score < 0 or score > 100:
    print("Ошибка диапазона")
elif score <= 49:
    print("Нужна доработка")
elif score <= 84:
    print("Зачёт")
elif score <= 100:
    print("Отличный результат")