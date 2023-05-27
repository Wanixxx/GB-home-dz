#ДЗ_3
'''
 Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.
'''

number_one = int(input())
number_two = int(input())
number_three = int(input())
def my_func(one, two, three):
    first_max = max(one, two, three)
    if max(one, two, three) == one:
        return first_max + max(two, three)
    elif max(one, two, three) == two:
        return first_max + max(one, three)
    elif max(one, two, three) == three:
        return first_max + max(one, two)

numbers_sum = my_func(one=number_one, two=number_two, three=number_three)
print(numbers_sum)