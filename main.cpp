#include <iostream>

/**
 * Рекурсивная функция вычисления факториала числа.
 * Факториал n! = n * (n-1) * ... * 1, при этом 0! = 1.
 * 
 * @param n неотрицательное целое число
 * @return факториал числа n
 */
long long factorial(int n) {
    // Базовый случай: 0! = 1 и 1! = 1
    if (n <= 1) {
        return 1;
    }
    // Рекурсивный случай: n! = n * (n-1)!
    return n * factorial(n - 1);
}

int main() {
    int number = 7;

    // Вызов функции
    long long result = factorial(number);

    std::cout << "Число: " << number << std::endl;
    std::cout << "Факториал: " << result << std::endl;

    return 0;
}
