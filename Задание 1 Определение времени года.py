a = int(input('Введите номер месяца '))
if 1<=a<=2:
    print('Зима')
elif 3<=a<=5:
    print('Весна')
elif 6<=a<=8:
    print('Лето')
elif 9<=a<=11:
    print('Осень')
elif a==12:
    print('Зима')
else:
    print('Ошибка, введите число от 1 до 12')