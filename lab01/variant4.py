name_order = input("Название заказа: ")
name = input("Ваше имя: ")
name_position1 = input("Название первой позиции: ")
name_position2 = input("Название второй позиции: ")
quantity1 = int(input(f"Количество предметов в позиции {name_position1}: "))
prise1 = float(input(f"Цена предмета в позиции {name_position1}: "))
quantity2 = int(input(f"Количество предметов в позиции {name_position2}: "))
prise2 = float(input(f"Цена предмета в позиции {name_position2}: "))
delivery_price = float(input("Ценна доставки: "))
deposited_amount = float(input("Внесённая сумма: "))
position_prise1 = prise1 * quantity1
position_prise2 = prise2 * quantity2
full_price = position_prise1 + position_prise2
full_prise_delivery = delivery_price + full_price
full_quantity = quantity1 + quantity2
change_price = deposited_amount - full_prise_delivery
print("----------")
print(f"Заказ {name_order}")
print(f"Имя заказчика: {name}")
print(f"{name_position1} - {quantity1}шт; {prise1:.2f}р/шт; {position_prise1:.2f}р")
print(f"{name_position2} - {quantity2}шт; {prise2:.2f}р/шт; {position_prise2:.2f}р")
print(f"Общее количество: {full_quantity}")
print(f"Общая сумма без учёта доставки/с учётом доставки: {full_price:.2f}р/{full_prise_delivery:.2f}")
print(f"Сдача: {change_price:.2f}")
print("----------")