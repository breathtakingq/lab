Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import sys
>>> def get_word():
	global word
	word=input('Введите слово:')
	if word.isalpha()==False:
		print('Ошибка ввода!!!')
		sys.exit()
	else:
		print('Успех')

		
>>> def is_palindrome():
    word_lower=word.lower()
    if word.lower()==word.lower()[::-1]:
        return True
    else:
        return False

>>> def is_palindrome_old():
	global what_is
	if word==word[::-1]:
		what_is='палиндром'
	else:
		what_is='не палиндром'

		
>>> def create_message():
	if is_palindrome():
		prefix=''
	else:
		prefix='не'
	msg=('Слово %s - %s %s' % (word,prefix, 'палиндром.'))
	return print(msg)

>>> def palindrome():
	get_word()
	is_palindrome()
	create_message()

	
>>> palindrome()
Введите слово:доход
Успех
Слово доход -  палиндром.
>>> palindrome()
Введите слово:топор
Успех
Слово топор - не палиндром.
>>> 