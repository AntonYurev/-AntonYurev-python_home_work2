# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# n = float(input('Введите число : '))
# s = 0
# str_n = str(n)
# str_n = str_n.replace('.', '')
# for i in range(len(str_n)):
#     s = s + int(str_n[i])
# print(s)

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
n = int(input('Введите число : '))
integral = 1
integral_list = []
for i in range (1, n+1):
    integral = integral * i
    integral_list.append(integral)
print(integral_list)

