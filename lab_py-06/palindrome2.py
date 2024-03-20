Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def get_word():
	global word
	word=input('Введите слово:')

	
>>> def is_palindrome():
	 global what_is
	 if word==word[::-1]: what_is='палиндром'
	 else: what_is='не палиндром'

	 
>>> def create_message():
	msg=('Слово %s - %s' % (word,what_is))
	return print(msg)

>>> def palindrome():
	get_word()
	is_palindrome()
	create_message()

	
>>> palindrome()
Введите слово:наган
Слово наган - палиндром
>>> palindrome()
Введите слово:таган
Слово таган - не палиндром
>>> 