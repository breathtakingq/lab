Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = 1000
>>> y = x
>>> id(x)
3088504848272
>>> id(y)
3088504848272
>>> x = 1001
>>> y = 1000
>>> id(x)
3088505769264
>>> id(y)
3088505769104
>>> id_x = 3088505769264
>>> id_y = 3088505769104
>>> a = "x = " + str(x) + " id = " + str(id_x)
>>> b = "y = " + str(y) + " id = " + str(id_y)
>>> print(a)
x = 1001 id = 3088505769264
>>> print(b)
y = 1000 id = 3088505769104
>>> 
================================ RESTART: Shell ================================
>>> x=2
>>> x*=2+#
SyntaxError: invalid syntax
>>> x=2
>>> x*=2+3
>>> print(x)
10
>>> 
================================ RESTART: Shell ================================
>>> x = 81
>>> x*=3
>>> print(x)
243
>>> x = 81
>>> id(x)
2372928820080
>>> x = 81
>>> x*=3
>>> print(x)
243
>>> id(x)
2372928825328
>>> x = 81
>>> x = 512
>>> id(x)
2372966505808
>>> x*=3
>>> print(x)
1536
>>> id(x)
2372966505584
>>> 
================================ RESTART: Shell ================================
>>> year = 2016
>>> next_day = "После 28 февраля будет "
>>> if (year % 4 == 0): next_dat += "29 февраля"
else: next_day += "1 марта"

Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    if (year % 4 == 0): next_dat += "29 февраля"
NameError: name 'next_dat' is not defined
>>> if (year % 4 == 0): next_day+= "29 февраля"
else: next_day += "1 марта"

>>> print(next_day)
После 28 февраля будет 29 февраля
>>> 
================================ RESTART: Shell ================================
>>> year = 2017
>>> next_day = "После 28 февраля будет "
>>> if (year % 4 == 0): next_day += "29 февраля"
else: next_day += "1 марта"

>>> print(next_day)
После 28 февраля будет 1 марта
>>> 