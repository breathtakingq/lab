Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ege2 = ["Математика - 78", "Информатика - 75", "Русский язык - 62"]
>>> lst3=[]
>>> lst4=[]
>>> def get_info():
	for k in range(len(ege2)):
		b=[]
		a=ege2[k].split('-')
		b.append(a[0]), b.append(int(a[1]))
		lst3.extend(b), lst4.append(b)

		
>>> def subjects():
	global sub
	sub=[]
	for k in range(0, len(lst3),2):
		sub.append(lst3[k])
	return print(sub)

>>> def marks():
	global mark
	mark=[]
	for i in range(-1, len(lst3)-1,2):
		mark.append(lst3[i])
	return print(mark)

>>> def print_results():
	get_info()
	subjects()
	marks()
	for k in range(len(lst3)//2):
		print(sub[k],'-',mark[k])
	print('Сумма баллов:',sum(mark))

	
>>> print_results()
['Математика ', 'Информатика ', 'Русский язык ']
[62, 78, 75]
Математика  - 62
Информатика  - 78
Русский язык  - 75
Сумма баллов: 215
>>> 