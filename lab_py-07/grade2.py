Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def grade2():
	points=int(input("Введите ваше количество баллов: "))
	if points<60:
		return print('Неудовлетворительно')
	elif points>=60 and points<=70:
		return print('Удовлетворительно')
	elif points>=71 and points<=84:
		return print('Хорошо')
	elif points>=85:
		return print('Отлично')

	
>>> grade2()
Введите ваше количество баллов: 84
Хорошо
>>> grade2()
Введите ваше количество баллов: 54
Неудовлетворительно
>>> 