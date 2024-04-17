def get_word_list_1():
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


get_word_list_1()
