while True:
    try:
        target = int(input("Введите искомую сумму: "))
        break
    except ValueError:
        print("Ошибка: сумма должна быть целым числом.")


# Поиск пар
pairs = []

for num in range(0, target + 1):  # от 0 до target
    complement = target - num
    if num <= complement:  # защита от дублей (a,b) и (b,a)
        pairs.append((num, complement))

# Вывод результата
print(f"Искомая сумма: {target}")

if pairs:
    print("Найденные пары")
    for i in pairs:
        print(i)
    print(f"Количество найденных пар: {len(pairs)}")
else:
    print("Пар с такой суммой не найдено.")
