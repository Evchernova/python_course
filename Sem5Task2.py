"""Подсчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5)."""

a = int(input("Введите натуральное число: "))
even = 0
odd = 0

while True:
    if a % 2 == 0:
        even += 1
    else:
        odd += 1

    a //= 10

    if a == 0:
        break

print(f'Количество четных цифры в введенном числе: {even}')
print(f'Количество нечетных цифры в введенном числе: {odd}')
