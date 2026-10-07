print("Рассчёт цены и сдачи:")
priсe = int(input("Цена одной тетради: "))
count = int(input("Количество тетрадей: "))
paid = int(input("Переданная сумма: "))
full_prise = priсe * count
change_price = paid - full_prise
print("----------")
print(f"Итог: {full_prise}р.")
print(f"Сдача: {change_price}р.")
print("----------")