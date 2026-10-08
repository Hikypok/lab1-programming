a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))

if a >= b and a >= c:
    maximum = a
elif b >= a and b >= c:
    maximum = b
else:
    maximum = c

print(f"Максимум: {maximum}")