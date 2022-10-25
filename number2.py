# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# n = float(input('Введите число : '))
# s = 0
# str_n = str(n)
# str_n = str_n.replace('.', '')
# for i in range(len(str_n)):
#     s = s + int(str_n[i])
# print(s)

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# n = int(input('Введите число : '))
# integral = 1
# integral_list = []
# for i in range (1, n+1):
#     integral = integral * i
#     integral_list.append(integral)
# print(integral_list)

# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.
# n = int(input('Введите число : '))
# sum = 0
# sum_list = []
# for i in range(1, n+1):
#     sum = sum + round((1 + 1 / i)**i, 2)
#     sum_list.append(f'{i} : ' + str(round((1 + 1 / i)**i, 2)) )
# print(sum_list)
# print('Сумма : ' + str(sum))

# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
# n = int(input('Введите число : '))
# mult = 1
# import random
# a = [-n]
# for i in range (1, n-1):
#     a.append(random.randint(-n,n))
# a.append(n)
# print('Наш список: ', a)
# for i in open('file.txt'):
#     mult = mult * a[int(i)]
# print('Произведение элементов= ', mult)

# Реализуйте алгоритм перемешивания списка.
# n = int(input('Введите число : '))
# reserve = 0
# a = []
# import random
# for i in range (0,n):
#     a.append(random.randint(-n,n))
# print('Наш список: ', a)
# for i in range (0,n*2):
#     k=random.randint(0,n-1)
#     l=random.randint(0,n-1)
#     reserve=a[k]
#     a[k]=a[-l]
#     a[-l]=reserve
# print('Перемешанный список: ', a)

# ДОП. задача на алгоритмы с реальных собеседований
# Даны два массива:
# [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2]
# Надо вернуть их пересечение
# [1, 2, 2, 3]
# (порядок не важен)
# a = [1, 2, 3, 2, 0]
# b = [5, 1, 2, 7, 3, 2]
# c = []
# for i in range (len(a)):
#     for j in range (len(b)):
#         if a[i] == b[j]:
#             c.append(a[i])
#             a[i]='t'
#             b[j]='n'
# print(c)


