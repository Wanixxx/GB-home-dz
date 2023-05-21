#ДЗ №3
'''
Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.
'''
number_one = int(input())
number_two = int(input())
number_three = int(input())

def my_func(one, two, three):
	first_max = max(one, two, three) #Найти самое большое число среди ввёднных и присвоить его переменной first_max
	if first_max == one: #Если самое большое число равно первому аргументу
		return first_max + max(two, three) #Верни самое большое число + самое большое число среди второго и третьего аргумента
	elif first_max == two:
		return first_max + max(one, three)
	elif first_max == three:
		return first_max + max(one, two)

numbers_sum = my_func(one = number_one, two = number_two, three = number_three)
print(numbers_sum)