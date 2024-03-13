Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> "%4.4f"%12.34
'12.3400'
>>> "%4.4f"%123456.78
'123456.7800'
>>> "%4.4f"%1234.56987
'1234.5699'
>>> "%4.0f"%1234.56987
'1235'
>>> 
================================ RESTART: Shell ================================
>>> x = 158.58
>>> print("Сумма покупки %s руб., скидка %s коп." % (x,x[4:]))
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print("Сумма покупки %s руб., скидка %s коп." % (x,x[4:]))
TypeError: 'float' object is not subscriptable
>>> x = "158.58"
>>> print("Сумма покупки %s руб., скидка %s коп." % (x,x[4:]))
Сумма покупки 158.58 руб., скидка 58 коп.
>>> 