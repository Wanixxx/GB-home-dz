number = int(input("Укажите месяц (числом): "))
if number <= 12 and number >= 1:
	month_dict = {
			1 : "Зима",
			2 : "Зима",
			3 : "Весна",
			4 : "Весна",
			5 : "Весна",
			6 : "Лето",
			7 : "Лето",
			8 : "Лето",
			9 : "Осень",
			10 : "Осень",
			11 : "Осень",
			12 : "Зима"}
	month_list = list(month_dict.values())
	for i, el in enumerate(month_list):
		if i == number-1:
			print({month_list[i]})
			break
			print({month_dict[number]})
	else:
		print("Неверно указано число.")