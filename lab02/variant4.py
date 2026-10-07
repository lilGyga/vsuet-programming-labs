total_parts = int(input("Общее количество деталей: "))
container_capacity = int(input("Вместимость одного контейнера: "))
full_containers = total_parts // container_capacity
remainder = total_parts % container_capacity
total_containers = (total_parts + container_capacity - 1) // container_capacity
print("----------")
print(f"Полностью заполненных контейнеров: {full_containers}")
print(f"Остаток деталей: {remainder}")
print(f"Всего понадобится контейнеров: {total_containers}")
print("----------")