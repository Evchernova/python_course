"""Реализовать структуру «Рейтинг», представляющую собой не
возрастающий набор натуральных чисел
(каждый элемент ряда меньше или равен предыдущему).
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них."""

my_list = [7, 5, 3, 3, 2]
print(f"Рейтинг - {my_list}")
digit = int(input("Введите число: "))
for i in range(len(my_list)):
    if my_list[i] == digit:
        my_list.insert(i + 1, digit)
        break
    elif my_list[0] < digit:
        my_list.insert(0, digit)
    elif my_list[-1] > digit:
        my_list.append(digit)
    elif my_list[i] > digit and my_list[i + 1] < digit:
        my_list.insert(i + 1, digit)
        break
print(f"Новый список - {my_list}")

