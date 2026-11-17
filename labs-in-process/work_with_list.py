import random

n = int(input("Введите число N: "))
nums = [random.randint(1, 100) for _ in range(n)]
print(f"Начальный список: {nums}")
print(f"Сумма чисел: {sum(nums)}")
print(f"Среднее: {sum(nums) / len(nums):.2f}")
print(f"Максимум: {max(nums)}")
print(f"Минимум: {min(nums)}")

nums.sort()  # сортировка списка
print(f"Отсортированный список: {nums}")

# удаление дубликатов с сохранением порядка
unique = list(dict.fromkeys(nums))
print(f"Без дубликатов: {unique}")
