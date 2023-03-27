"""Определить, какие из слов «attribute», «класс», «функция», «type»
 невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode)."""

words = ['attribute', 'класс', 'функция', 'type']

try:
    for el in words:
        f = bytes(el, 'ascii')
        print(f"тип: {type(f)}, содержимое:  {f}")
except UnicodeEncodeError:
    print(f"Заданное слово - {el}. Ошибка, заданное слово должно быть на латинице.")