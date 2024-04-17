import sys
def get_word_2():
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


get_word_2()

