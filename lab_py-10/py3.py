Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def get_word_list_1():
	user_list=input('Введите список слов в формате [..., ..., ...] : ')
	word_list=eval(user_list)
	list=[]
	for k in word_list:
		if isinstance(k,str) and k.isalpha():
			list.append(k)
		elif isinstance(k,int):
			print('%s - не является строкой' % k)
	if len(list)!=0:
		return print(list)
	else:
		return print('Проблема с исходными данными!')

	
>>> get_word_list_1()
Введите список слов в формате [..., ..., ...] : ["первый", "второй", "третий"]
['первый', 'второй', 'третий']
>>> get_word_list_1()
Введите список слов в формате [..., ..., ...] : ["первый", 2, "третий"]
2 - не является строкой
['первый', 'третий']
>>> get_word_list_1()
Введите список слов в формате [..., ..., ...] : [1, 2, 3]
1 - не является строкой
2 - не является строкой
3 - не является строкой
Проблема с исходными данными!
>>> 