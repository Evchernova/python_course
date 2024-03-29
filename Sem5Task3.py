"""Сформировать из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
то надо вывести число 6843."""


def reverse(n, i):
    if n == 0:
        return i
    else:
        return reverse(n // 10, i * 10 + n % 10)


a = int(input("Введите число: "))
print(f'Число с обратным порядком цифр: {reverse(a, 0)}')
