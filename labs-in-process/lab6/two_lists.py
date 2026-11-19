list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Способ 1: Через множества
set1 = set(list1)
set2 = set(list2)

union = set1 | set2
intersection = set1 & set2
difference = set1 - set2

print(f"Объединение: {sorted(union)}")  # [1, 2, 3, 4, 5, 6, 7, 8]
print(f"Пересечение: {sorted(intersection)}")  # [4, 5]
print(f"Разность: {sorted(difference)}")  # [1, 2, 3]


# Способ 2: Через List Comprehension
# Добавляем к list1 только те элементы из list2, которых ещё нет в list1
union_ordered = list1 + [x for x in list2 if x not in list1]

# Оставляем только те элементы из list1, которые есть в list2
intersection_ordered = [x for x in list1 if x in list2]

# Оставляем элементы из list1, которых НЕТ в list2
difference_ordered = [x for x in list1 if x not in list2]

print("\nС сохранением порядка:")
print(f"Объединение: {union_ordered}")  # [1, 2, 3, 4, 5, 6, 7, 8]
print(f"Пересечение: {intersection_ordered}")  # [4, 5]
print(f"Разность: {difference_ordered}")  # [1, 2, 3]
