# Напишите программу, которая определяет, является число четным или нечетным.

# Формат входных данных
# На вход программе подаётся одно целое число.

# Формат выходных данных
# Программа должна вывести «Четное», если число четное, и «Нечетное» — если число нечетное.

# code

a = int(input())

if a % 2 == 0:
    print("Четное")
else:
    print("Нечетное")
