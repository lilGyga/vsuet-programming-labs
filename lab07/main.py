from functions import sum_digits, average, normalize_text, select_numbers


def main():
    print("Демонстрация работы функций")
    number = int(input("Введите целое число: "))
    
    numbers = []
    for part in input("Введите целые числа через пробел: ").split():
        numbers.append(int(part))
        
    text = input("Введите произвольный текст: ")
    threshold = int(input("Введите порог для отбора чисел: "))
    
    print("----------")
    print(f"Сумма цифр числа: {sum_digits(number)}")
    
    avg = average(numbers)
    if avg is None:
        print("Среднее значение: Нет данных")
    else:
        print(f"Среднее значение: {avg:.2f}")
        
    print(f"Нормализованный текст: {normalize_text(text)}")
    print(f"Числа не меньше порога: {select_numbers(numbers, threshold)}")
    print("----------")


if __name__ == "__main__":
    main()