"""Пользователь вводит строку из нескольких слов,
разделённых пробелами. Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если слово длинное,
выводить только первые 10 букв в слове."""

my_str = input("Введите несколько слов через пробел: ")
words = []
i = 1
for elem in range(my_str.count(' ') + 1):
    words = my_str.split()
    if len(str(words)) <= 10:
        print(f"{i}. {words[elem]}")
        i += 1
    else:
        print(f"{i}. {words[elem][0:10]}")
        i += 1

