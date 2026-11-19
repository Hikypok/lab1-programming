nums = [1, 2, 3, 2, 3, 1, 6, 7, 6, 7, 8, 9, 23, 21, 232, 23]
from collections import Counter

# Способ 1: Использование множеств
seen = set()  # хранит все уникальные числа, которые мы уже встретили
dublicates1 = set()  # будет содержать только те числа, что встретились повторно
for num in nums:
    if num in seen:  # Если число уже есть в seen, значит оно повторяется
        dublicates1.add(num)
    # Добавляем текущее число в множество просмотренных
    seen.add(num)

print(f"Дубликаты: {list(dublicates1)}")

# Способ 2: Использование Counter
counts = Counter(nums)  # Создаём словарь вида {число: количество_вхождений}
# Counter - специальный класс для подсчёта элементов коллекции
# Формирую список из элементов, у которых значение счётчика больше 1
dublicates2 = [num for num, count in counts.items() if count > 1]

print(f"Дубликаты: {dublicates2}")
