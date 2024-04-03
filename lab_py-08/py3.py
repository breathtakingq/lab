Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ege4 = [["Математика",78], ["Информатика", 75], ["Русский язык", 62]]
>>> (ege4[1])[0]
'Информатика'
>>> ege = ege4
>>> def total(ege):
	math = (ege[0])[1]
	inf = (ege[1])[1]
	rus = (ege[2])[1]
	return math+inf+rus

>>> summ = total(ege)
>>> 
>>> print("Общая сумма баллов: %d"% summ)
Общая сумма баллов: 215
>>> ege3 = ["Математика", 78, "Информатика", 75, "Русский язык", 62]
>>> def total2(ege3):
	global total2
	math = ege3[1]
	inf = ege3[3]
	rus = ege3[5]
	return math+inf+rus

>>> summ2 = total2(ege3)
>>> print ("Общая сумма баллов: %d"% summ2)
Общая сумма баллов: 215
>>> def convert_list(ege):
	global ege4
	ege4 = []
	math = ege3[1]
	inf = ege3[3]
	rus = ege3[5]
	ege4.extend([math, inf, rus])
	return ege4

>>> def total():
	convert_list(ege)
	math = (ege4[0])[1]
	inf = (ege4[1])[1]
	rus = (ege4[2])[1]
	return math+inf+rus

>>> summ3 = total()
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    summ3 = total()
  File "<pyshell#29>", line 3, in total
    math = (ege4[0])[1]
TypeError: 'int' object is not subscriptable
>>> def total():
	convert_list(ege)
	math = (ege[0])[1]
	inf = (ege[1])[1]
	rus = (ege[2])[1]
	return math+inf+rus

>>> summ3 = total()
>>> print ("Общая сумма баллов: %d"% summ3)
Общая сумма баллов: 215
>>> 