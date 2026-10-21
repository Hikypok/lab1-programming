n = int(input("Введите число: "))
original = n
factors = []

divisor = 2

# Делим число на 2, пока делится. Потом на 3, потом на 5 и т.д.
while divisor ** 2 <= n:  # Оптимизация: проверяем делители до √n
    while n % divisor == 0:
        factors.append(divisor)
        n //= divisor
    divisor += 1

if n > 1: # Если после всех делений n > 1, значит оставшееся число - простой множитель
    factors.append(n)

# Преобразуем список чисел в строку вида "2 x 3 x 5"
print(f"{original} = {" x ".join(map(str, factors))}")