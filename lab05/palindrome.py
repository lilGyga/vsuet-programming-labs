print("Проверка на палиндром")
text = input("Введите текст: ")

cleaned_text = text.replace(" ", "").lower()

print("----------")
if len(cleaned_text) == 0:
    print("Нет текста")
elif cleaned_text == cleaned_text[::-1]:
    print("Палиндром")
else:
    print("Не палиндром")
print("----------")