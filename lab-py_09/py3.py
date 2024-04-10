Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ege1 = "Математика — 78,      Информатика — 75, Русский язык — 62"
>>> def convert_list14(ege1):
	ege4=[]
	ege=ege1.split(',')
	for k in range(len(ege)):
		ege2=ege[k].strip()
		ege3=ege2.split('—')
		for i in range(2):
			c=ege3[i].strip()
			ege4.append(c)
	ege_new=[]
	math = ege4[0:2]
	inf = ege4[2:4]
	rus = ege4[4:6]
	ege_new.extend([math, inf, rus])
	return print(ege_new)

>>> convert_list14(ege1)
[['Математика', '78'], ['Информатика', '75'], ['Русский язык', '62']]
>>> 