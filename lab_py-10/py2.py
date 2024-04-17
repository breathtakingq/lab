Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import sys
>>> def get_word_2():
	max_attempts=3
	for attempts in range(max_attempts):
		word=input('Введите слово: ')
		if word.isalpha():
			break
		else:
			if attempts==max_attempts-1:
				print('Выполнено %d неудачных попыток. Выход из программы.' % max_attempts)
				sys.exit()
			else:
				print('Повторите ввод!')

				
>>> get_word_2()
Введите слово: asd
>>> get_word_2()
Введите слово: asd1
Повторите ввод!
Введите слово: 
Повторите ввод!
Введите слово: asd
>>> get_word_2()
Введите слово: 13a
Повторите ввод!
Введите слово: 54
Повторите ввод!
Введите слово: 44
Выполнено 3 неудачных попыток. Выход из программы.
>>> 