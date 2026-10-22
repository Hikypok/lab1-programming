n = 5

# Прямоугольник
print("Прямоугольник:")
for i in range(n):
    print("*" * n)

# Треугольник
print("\nТреугольник:")
for i in range(1, n + 1):
    print("*" * i)

# Ёлочка
print("\nЁлочка:")
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# Poмб
print("\nPoмб:")
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))
