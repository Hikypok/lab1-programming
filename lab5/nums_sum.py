n = int(input("Введите N: "))

sum_numbers = 0
product = 1  # Начальное значение для вычисления факториала (N!)
sum_squares = 0

# Вычисляем сумму чисел, факториал и сумму квадратов за один проход
for i in range(1, n + 1):
    sum_numbers += i
    product *= i
    sum_squares += i ** 2

print(f"Cyммa: {sum_numbers}")
print(f"Произведение (N!): {product}")
print(f"Сумма квадратов: {sum_squares}")