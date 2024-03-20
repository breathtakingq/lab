Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> var1='Глобальная'
>>> def my_func():
	print(var1)

	
>>> my_func()
Глобальная
>>> def my_func():
	var1='Глобальная'
	var1='Локальная'
	print(var1)

	
>>> my_func()
Локальная
>>> def my_func():
	var1='Локальная'
	var1='Глобальная'
	print(var1)

	
>>> my_func()
Глобальная
>>> def my_func():
	global var1
	var1='Локальная'
	var1='Глобальная'
	print(var1)

	
>>> 
>>> my_func()
Глобальная
>>> def my_func():
	global var1
	var1='локальная'
	var2='вторая'
	print(var1)
	print(var2)

	
>>> my_func()
локальная
вторая
>>> def my_func():
	global var1
	var1='локальная'
	var2='вторая'

	
>>> my_func()
>>> print(var1)
локальная
>>> print(var2)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    print(var2)
NameError: name 'var2' is not defined
>>> def my_func():
	global var1, var2
	var1='локальная'
	var2='вторая'

	
>>> my_func()
>>> print(var1)
локальная
>>> print(var2)
вторая
>>> 