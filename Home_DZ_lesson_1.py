##Задание №1
	number = int(input("Какой сегодня число? "))
	words = str(input("Какой сегодня месяц? "))
	b = number
	c = words
	print(b, c)

## Задание № 2
time = int(input("Укажите колличество секунд"))
clock = time / 3600 #Колличество часов;
minutes = time / 60 #Колличество минут;
print('Часы = '%clock, 'Минуты = '%minutes, 'Секунды = '%time)

## Задание № 3
n = int(input("Введите число: "))
total = (n + int(str(n) + str(n) + int(str(n) + str(n) + str(n))))
print("Сумма чисел n + nn + nnn - %d" % total)


## Задание №4

number = int(input("Введите положительное число: "))
max = number % 10
while number >= 1:
	number = number//10
	if number%10 > max:
		max = number % 10
	if number > 9:
		continue
	else:
		print(max)
		break

## Задание №5 и 6
profit = float(input("Введите выручку фирмы "))
costs = float(input("Введите издержки фирмы "))
if profit > costs:
    print(f"Фирма работает с прибылью. Рентабельность выручки составила {profit / costs:.2f}")
    workers = int(input("Введите количество сотрудников фирмы "))
    print(f"прибыль в расчете на одного сторудника сотавила {profit / workers:.2f}")
elif profit == costs:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")
