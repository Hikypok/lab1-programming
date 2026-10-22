n = int(input("Введите число: "))
original = n

count = 0  # количество цифр
total = 0  # сумма цифр
product = 1  # произведение цифр
reversed_num = 0  # перевернутое число

while n > 0:  # разибраем число на цифры спава налево
    digit = n % 10
    count += 1
    total += digit
    product *= digit
    reversed_num = reversed_num * 10 + digit  # сдвигаем старое число влево и добавляем новую цифру
    n //= 10

print(f"Количество цифр: {count}")
print(f"Сумма цифр: {total}")
print(f"Произведение цифр: {product}")
print(f"Перевёрнутое число: {reversed_num}")