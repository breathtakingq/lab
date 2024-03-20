Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def get_word():
	word=input('Введите слово:')
	return word

>>> def is_palindrome(word):
	if word==word[::-1]:
		what_is='палиндром'
		else:
			
SyntaxError: invalid syntax
>>> def is_palindrome(word):
	if word==word[::-1]: what_is='палиндром'
	else: what_is='не палиндром'
	return what_is

>>> def create_message(word,what_is):
	msg=('Слово %s - %s' % (word,what_is))
	return print(msg)

>>> def palindrome():
	x=get_word()
	y=is_palindrome(x)
	z=create_message(x,y)
	return z

>>> z
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    z
NameError: name 'z' is not defined
>>> print(palindrome())
Введите слово:наган
Слово наган - палиндром
None
>>> palindrome()
Введите слово:таган
Слово таган - не палиндром
>>> palindrome()
Введите слово:
Слово  - палиндром
>>> 