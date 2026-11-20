import random

# Запрашиваем у пользователя количество элементов списка
n = int(input("Введите число N: "))

# Генерируем список из n случайных целых чисел от 1 до 100
nums = [random.randint(1, 100) for _ in range(n)]

print(f"Начальный список: {nums}")
print(f"Сумма чисел: {sum(nums)}")
print(f"Среднее: {sum(nums) / len(nums):.2f}")
print(f"Максимум: {max(nums)}")
print(f"Минимум: {min(nums)}")

# Сортируем список по возрастанию (изменяет сам список nums)
nums.sort()
print(f"Отсортированный список: {nums}")

# удаление дубликатов с сохранением порядка
# dict.fromkeys() создаёт словарь, где ключи - уникальные значения списка
unique = list(dict.fromkeys(nums))
print(f"Без дубликатов: {unique}")
