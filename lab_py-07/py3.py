Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import sys
>>> def get_word():
	global word
	word=input('Введите слово:')
	if word.isalpha()==False:
		if word=='':
			return sys.exit("Пустая строка")
		else:
			return sys.exit('Недопустимый символ')
	else:
		print('Успех')

		
>>> get_word()
Введите слово:
SystemExit: Пустая строка
>>> get_word()
Введите слово:доход
Успех
>>> get_word()
Введите слово:доход11
SystemExit: Недопустимый символ
>>> 