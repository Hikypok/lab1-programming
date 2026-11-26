# создаем функцию, явно указывая типы входных и выходных данных
def count_words(text: str) -> int:
    """функция возвращает количество слов в тексте"""
    # .split() разбивает текст на список подстрок
    # len() считает количество элементов в списке
    return len(text.split())


# использование
text = input("Введите текст: ")
print(f"Количество слов: {count_words(text)}")

# не делала с использованием re, тк у меня он некорректно работает почему-то


def count_words_clean(text: str) -> int:
    """функция подсчитывает слова, игнорируя пунктуацию"""
    clean_text = ""
    for char in text:
        # если символ - буква или цифра или пробел, оставляем его
        # isalnum() возвращает True для букв и цифр
        # isspace() возвращает True для пробелов
        if char.isalnum() or char.isspace():
            clean_text += char

    # теперь считаем слова в очищенном тексте
    return len(clean_text.split())


print(f"Слов (с пунктуацией): {count_words(text)}")
print(f"Слов (без пунктуации): {count_words_clean(text)}")
