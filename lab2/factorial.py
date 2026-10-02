def factorial(n: int) -> int:
    """
    Рекурсивная функция вычисления факториала числа.

    Факториал n! = n * (n-1) * ... * 2 * 1, при этом 0! = 1.

    Args:
        n: неотрицательное целое число

    Returns:
        факториал числа n
    """
    # Базовый случай: 0! = 1 и 1! = 1
    if n <= 1:
        return 1
    # Рекурсивный случай: n! = n * (n-1)!
    return n * factorial(n - 1)


# Проверка работы функции
if __name__ == "__main__":
    number = 7
    result = factorial(number)
    print(f"Факториал числа {number} = {result}")
