from functions import average, normalize_text, sum_digits, select_numbers

assert sum_digits(0) == 0
assert sum_digits(507) == 12
assert sum_digits(-507) == 12
assert average([]) is None
assert average([2, 4, 6]) == 4
assert abs(average([1, 2]) - 1.5) < 1e-9
assert normalize_text("  ПРИВЕТ   Мир  ") == "привет мир"
assert normalize_text("   ") == ""

assert select_numbers([-5, 0, 2, 5], 2) == [2, 5]
assert select_numbers([-5, 0, 1], 5) == []
assert select_numbers([], 2) == []
assert select_numbers([1, 2, 3], 2) == [2, 3]
assert select_numbers([2, 0, 2, 5, 2], 2) == [2, 2, 5, 2]

original = [-5, 0, 2, 5]
saved_copy = original.copy()
select_numbers(original, 2)
assert original == saved_copy

print("----------")
print("Базовые проверки и тесты варианта 4 успешно пройдены!")
print("----------")