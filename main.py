"""
Написать программу, которая:
- Создаёт случайный список из 20 значений по 4 случайных целых чисел от -10 до 10.
- Находит все уникальные комбинации пар из этих значений и выводит их в виде списка кортежей.
- Пользователь вводит целое число.
- Вычисляет количество пар, чья сумма меньше заданного пользователем значения.
"""
import random #Библиотека
count = 0 #Счетчик
list = [] #Список
list_tuple = [] #Список кортежей
unique = [] #Список уникальных комбинаций
num = int(input("Введите число: ")) #Вводим число 
for i in range(0,20): #Перебор
    list = [random.randint(-10,10) for j in range(4)] #Заполняем список
    list_tuple.append(list) #Добавляем список в список
for i in list_tuple: #Перебор
    if i not in unique: #Условие
        unique.append(i) #Добавляем i в список
        if sum(i) < num: #Условие
            count += 1
print(f"уникальные значения {tuple(unique)}")
print(f"счетчик комбинаций,чья сумма меньше,чем число пользователя {count}")
