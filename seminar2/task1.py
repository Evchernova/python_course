"""Спортсмен занимается ежедневными пробежками.
В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня,
на который результат спортсмена составит не менее b километров.
Программа должна принимать значения параметров a и b
и выводить одно натуральное число — номер дня."""

a = int(input("Введите результат пробежки первого дня в км: "))
b = int(input("Введите необходимый результат в км: "))
day_num = 1
while a < b:
         a = a + 0.1 * a
         day_num += 1
print(f"Номер дня, на который результат составит не менее {b} км - это  {day_num} день")