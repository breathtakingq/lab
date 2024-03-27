Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def grade1():
	mark=int(input('Введите оценку: '))
	if mark==2:
		return print('Не удовлетворительно')
	elif mark==3:
		return print('Удовлетворительно')
	elif mark==4:
		return print('Хорошо')
	elif mark==5:
		return print('Отлично')
	else:
		return print('Такой оценки нет.')

	
>>> grade1()
Введите оценку: 4
Хорошо
>>> grade1()
Введите оценку: 7
Такой оценки нет.
>>> 