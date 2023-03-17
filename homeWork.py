# Задача 2: Найдите сумму цифр трехзначного числа.
#
# *Пример:*
#
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

# number = input("Enter a three-digit number: ")
# sum_num = int(number[0]) + int(number[1]) + int(number[2])
# print(number, "->", sum_num, "(", number[0], "+", number[1], "+", number[2], ")")

# number = int(input("Enter a three-digit number: "))
# if 99 < number < 1000:
#     digit1 = number % 10
#     number1 = number // 10
#     digit2 = number1 % 10
#     number2 = number1 // 10
#     digit3 = number2 % 10
#     number3 = number2 // 10
#     print(number, "->", digit1 + digit2 + digit3, "(" ,digit3, "+", digit2, "+", digit1, ")")
# else:
#     print("You entered not a three-digit number. Try again, please.")

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
#
# *Пример:*
#
# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10

# S = int(input("Enter a three-digit number: "))
# if S % 6 == 0:
#     p_and_s = S // 3
#     p = p_and_s // 2
#     s = p_and_s // 2
#     k = p * 4
#     print(S, "->", p, k, s)
# else:
#     print("With value", S, "the task has no integer values")

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
#
# *Пример:*
#
# 385916 -> yes
# 123456 -> no

# number = input("Enter your ticket number: ")
# if 5 < len(number) < 7:
#     first_part = int(number[0]) + int(number[1]) + int(number[2])
#     second_part = int(number[3]) + int(number[4]) + int(number[5])
#     if first_part == second_part:
#         print(number, "-> yes")
#     else:
#         print(number, "-> no")
# else:
#     print("You entered an invalid number. Try again, please.")

# number = int(input("Enter your ticket number: "))
# if 99999 < number < 1000000:
#     digit1 = number % 10
#     number1 = number // 10
#     digit2 = number1 % 10
#     number2 = number1 // 10
#     digit3 = number2 % 10
#     number3 = number2 // 10
#     digit4 = number3 % 10
#     number4 = number3 // 10
#     digit5 = number4 % 10
#     number5 = number4 // 10
#     digit6 = number5 % 10
#     first_half = digit1 + digit2 + digit3
#     second_half = digit4 + digit5 + digit6
#     if first_half == second_half:
#         print(number, "-> yes")
#     else:
#         print(number, "-> no")
# else:
#     print("You entered an invalid number. Try again, please.")

# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).
#
# *Пример:*
#
# 3 2 4 -> yes
# 3 2 1 -> no

# n = int(input("Enter number n: "))
# m = int(input("Enter number m: "))
# k = int(input("Enter number k: "))
#
# if k >= n * m:
#     print("You entered the wrong amount. Please, try again.")
# else:
#     if k % n == 0 or k % m == 0:
#         print(n, m, k, "-> yes")
#     else:
#         print(n, m, k, "-> no")




