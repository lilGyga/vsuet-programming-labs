print("Введите данные для расчёта чебной нагрузки:")
subject1 = input("Введите ваш первый предмет: ")
subject2 = input("Введите ваш второй предмет: ")
quantity1 = int(input(f"Количество занятий по предмету {subject1}: "))
quantity2 = int(input(f"Количество занятий по предмету {subject2}: "))
timesub1 = float(input(f"Длительность одного занятия по предмету {subject1} в минутих: "))
timesub2 = float(input(f"Длительность одного занятия по предмету {subject2} в минутах: "))
freetime = float(input("Доступное время за неделю в часах: "))
print("----------")
print("Учебная нагрузка")
fulltime1 = quantity1*timesub1
fulltime2 = quantity2*timesub2
print(f"Время по предмету {subject1}:", fulltime1,"м")
print(f"Время по предмету {subject2}:", fulltime2,"м")
print(f"Общая нагрузка за неделю: {(fulltime1+fulltime2)/60:.2f}ч или {fulltime1+fulltime2}м")
print(f"Остаток свободного времени: {freetime-((fulltime1+fulltime2)/60):.2f}ч")
print(f"Нагрузка за 4 недели: {((fulltime1+fulltime2)*4)/60:.2f}ч")
print("----------")



