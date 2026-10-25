print("Нормализация текста")
text = input("Введите текст: ")

normalized = " ".join(text.split())
word_count = len(normalized.split())

print("----------")
print(f"Исходная длина: {len(text)}")
print(f"Новая длина: {len(normalized)}")
print(f"Нормализованный текст: {normalized}")
print(f"Количество слов: {word_count}")
print("----------")