print("Перевод секунд в часы,минуты и секунды:")
total_second = int(input("Введите общее количество секунд: "))
hours = total_second // 3600
minutes = total_second // 60 % 60
seconds = total_second % 60
print(f"{hours} ч. {minutes} мин. {seconds} с.")