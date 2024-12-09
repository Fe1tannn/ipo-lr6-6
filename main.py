import random 
count = 0
list = []
list_tuple = []
unique = []
num = int(input("Введите число: "))
for i in range(0,20):
    list = [random.randint(-10,10) for j in range(4)]
    list_tuple.append(list)
for i in list_tuple:
    if i not in unique:
        unique.append(i)
        if sum(i) < num:
            count += 1
print(f"уникальные значения {tuple(unique)}")
print(f"счетчик комбинаций,чья сумма меньше,чем число пользователя {count}")