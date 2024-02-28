Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 'a'<'а'
True
>>> ord('a')
97
>>> ord('а')
1072
>>> 
================================ RESTART: Shell ================================
>>> 1.0 or 1/0
1.0
>>> 1/0 or 1.0
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    1/0 or 1.0
ZeroDivisionError: division by zero
>>> "" and 1 or "123"
'123'
>>> 
================================ RESTART: Shell ================================
>>> "102"[1] and "102"[-1]
'2'
>>> 
================================ RESTART: Shell ================================
>>> 2%2==0 and 3%3==0
True
>>> 