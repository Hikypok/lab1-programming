number = int(input("Введите число:"))
if number % 2 == 0:
    print(f"Число {number} - чётное")
else:
    print(f"Число {number} - нечётное")

# ДОП ЗАДАНИЕ: определить, делится ли число на 3
if number % 3 == 0:
    print(f"Число {number} делится на 3")
else:
    print(f"Число {number} не делится на 3")

# ДОП ЗАДАНИЕ: определить, является ли число положительным, отрицательным, нулем
if number > 0:
    print(f"Число {number} - положительное")
elif number == 0:
    print(f"Число {number} - нуль")
else:
    print(f"Число {number} - отрицательное")