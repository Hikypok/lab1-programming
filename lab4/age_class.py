try:
    age = int(input("Введите возраст: "))
    if age < 0:
        print("Некорректный возраст")
    elif age <= 12:
        print("Ребёнок")
    elif age <= 17:
        print("Подросток")
    elif age <= 64:
        print("Взрослый")
    elif age > 64 and age < 200:
        print("Пожилой")
    else:
        print("Ты инопланетянин?")
except TypeError:
    print("Это не число! Введите число!!")