Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> year = 2016
>>> next_day = "После 28 февраля будет "
>>> if year % 4 == 0 and year%100!=0 or year%400==0: next_day+= "29 февраля"
else: next_day += "1 марта"

>>> print(next_day)
После 28 февраля будет 29 февраля
>>> 
================================ RESTART: Shell ================================
>>> year = 2017
>>> next_day = "После 28 февраля будет "
>>> if year % 4 == 0 and year%100!=0 or year%400==0: next_day+= "29 февраля"
else: next_day += "1 марта"

>>> print(next_day)
После 28 февраля будет 1 марта
>>> 