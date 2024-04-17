Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def get_word_1():
	no_data=True
	while no_data:
		word=input('Введите слово: ')
		if word.isalpha():
			no_data=False
		else:
			print('Повторите ввод!')
	return word

>>> get_word_1()
Введите слово: fff1
Повторите ввод!
Введите слово: 
Повторите ввод!
Введите слово: asd
'asd'
>>> 