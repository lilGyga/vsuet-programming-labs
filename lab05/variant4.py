print("Поиск слов на букву 'к'")
text = input("Введите текст: ")
words = text.split()

match_count = 0

print("----------")
for word in words:
    cleaned_word = word.strip(".,!?;:").lower()
    if len(cleaned_word) > 0 and cleaned_word.startswith("к"):
        print(cleaned_word)
        match_count += 1

if match_count == 0:
    print("Нет совпадений")
else:
    print(f"Количество совпадений: {match_count}")
print("----------")