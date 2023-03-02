"""Создать список и заполнить его элементами различных типов данных.
Реализовать проверку типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе."""

one_list = [5.6, False, None, -1, 'helloWorld',  4]
def check_type(i):
     for i in range(len(one_list)):
         print(type(one_list[i]))
     return
print(one_list)
check_type(one_list)
