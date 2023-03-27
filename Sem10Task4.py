"""Преобразовать слова «разработка», «администрирование», «protocol»,
 «standard» из строкового представления в байтовое и выполнить
 обратное преобразование (используя методы encode и decode)."""

words = ['разработка', 'администрирование', 'protocol', 'standard']

for el in words:
    in_bytes = el.encode("utf-8")
    print(f"тип: {type(in_bytes)}, содержание:  {in_bytes}")

    in_str = in_bytes.decode("utf-8")
    print(f"тип: {type(in_str)}, содержание:  {in_str}")
