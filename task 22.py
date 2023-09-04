"""
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
повторениями). Выдать без повторений в порядке возрастания все те числа, которые
встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
элементов второго множества. Затем пользователь вводит сами элементы множеств

Пример:
11 6
2 4 6 8 10 12 10 8 6 4 2
3 6 9 12 15 18
6 12
"""

n = int(input("Enter a number N: "))
m = int(input("Enter a number M: "))
list_input_1 = list ()
list_input_2 = list ()

for i in range(n):
    list_input_1.append(int(input("Enter a value list_1: ")))
for i in range(m):
    list_input_2.append(int(input("Enter a value list_2: ")))
list_input_11 = set(list_input_1)
list_input_22 = set(list_input_2)
list = list_input_11.intersection(list_input_22)
list_1 = sorted(list)
print(list_1)