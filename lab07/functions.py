def sum_digits(number):
    num = abs(number)
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total


def average(numbers):
    if len(numbers) == 0:
        return None
    return sum(numbers) / len(numbers)


def normalize_text(text):
    return " ".join(text.lower().split())


def select_numbers(numbers, threshold):
    result = []
    for num in numbers:
        if num >= threshold:
            result.append(num)
    return result