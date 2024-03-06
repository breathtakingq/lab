Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> int(3.9999999)
3
>>> int(2.5)
2
>>> int(-2.3)
-2
>>> int(true)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    int(true)
NameError: name 'true' is not defined
>>> int(True)
1
>>> 
================================ RESTART: Shell ================================
>>> float(999)
999.0
>>> float('-1.25e-3')
-0.00125
>>> float(True)
1.0
>>> float('False')
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    float('False')
ValueError: could not convert string to float: 'False'
>>> 
================================ RESTART: Shell ================================
>>> int(1+2j)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    int(1+2j)
TypeError: can't convert complex to int
>>> float(1+2j)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    float(1+2j)
TypeError: can't convert complex to float
>>> 
================================ RESTART: Shell ================================
>>> a = int(input('Первое слагаемое: '))
Первое слагаемое: 3
>>> b = int(input('Второе слагаемое: '))
Второе слагаемое: 5
>>> c = a + b
>>> print(c)
8
>>> 
================================ RESTART: Shell ================================
>>> 'Да' if input("Введите что-то: ") else "Нет"
Введите что-то: 1
'Да'
>>> 'Да' if input("Введите что-то: ") else "Нет"
Введите что-то: 
'Нет'
>>> 