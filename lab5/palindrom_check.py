print("Первый способ(арифметический):")
n = int(input("Введите число: "))
original = n
reversed_num = 0 # перевернутое число

temp = n
while temp > 0:  # разибраем число на цифры справа налево
    digit = temp % 10
    reversed_num = reversed_num * 10 + digit  # сдвигаем старое число влево и добавляем новую цифру
    temp //= 10

if original == reversed_num:
    print(f"{original} - палиндром")
else:
    print(f"{original} - не палиндром")

print("Второй способ(через строки):")
text = input("Введите строку: ")
if text == text[::-1]:
    print("Палиндром")
else:
    print("Не палиндром")