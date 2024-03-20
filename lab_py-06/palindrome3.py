Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import sys
>>> def get_word():
	global word
	word=input('Введите слово:')
	if word=='':
		print('Ошибка')
		sys.exit()
	else:
		print('Успех')

		
>>> def is_palindrome():
	global what_is
	if word==word[::-1]:
		what_is='палиндром'
	else:
		what_is='не палиндром'

		
>>> def create_message():
	msg=('Слово %s - %s' % (word,what_is))
	return print(msg)

>>> def palindrome():
	get_word()
	is_palindrome()
	create_message()

	
>>> palindrome()
Введите слово:наган
Успех
Слово наган - палиндром
>>> palindrome()
Введите слово:таган
Успех
Слово таган - не палиндром
>>> 