print("Замена с подсчётом")
text = input("Введите текст: ")

count_replace = text.count(":")
new_text = text.replace(":", "-")

print("----------")
print(f"Количество замен: {count_replace}")
print(f"Новая строка: {new_text}")
print("----------")