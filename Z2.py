# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

lst = list(map(int, input("Введите числа через пробел:\n").split()))
l = 0
if len(lst) % 2 != 0:
    l = len(lst)//2 + 1
    new_lst = [lst[i]*lst[len(lst)-i-1] for i in range(l)]
    print(new_lst) 
else:
    l = len(lst)//2
    new_lst = [lst[i]*lst[len(lst)-i-1] for i in range(l)]
    print(new_lst)

