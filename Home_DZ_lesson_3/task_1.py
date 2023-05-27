#ДЗ_1
'''Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль. '''
number_one = int(input())
number_two = int(input())
def funck (number_one, number_two):
    if number_two == 0:
        return "На ноль делить нельзя!"
    return number_one / number_two
print(funck(number_one, number_two))