Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def number_of_solutions():
	a=int(input('Введите значение a: '))
	b=int(input('Введите значение b: '))
	c=int(input('Введите значение c: '))
	dis=b**2-4*a*c
	if dis<0:
		return print('Нет действительных корней')
	else:
		if dis==0:
			return print('Два равных корня')
		else:
			return print('Два различных корня')

		
>>> number_of_solutions()
Введите значение a: 1
Введите значение b: 1
Введите значение c: 1
Нет действительных корней
>>> number_of_solutions()
Введите значение a: 1
Введите значение b: 2
Введите значение c: 1
Два равных корня
>>> number_of_solutions()
Введите значение a: 1
Введите значение b: -3
Введите значение c: 2
Два различных корня
>>> 