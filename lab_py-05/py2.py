Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> "0123456789"[1:9:3]
'147'
>>> "0123456789"[::2]
'02468'
>>> 
================================ RESTART: Shell ================================
>>> x = "1a2b3c4d5e6f"
>>> print(x[::2] + x[1::2])
123456abcdef
>>> 
================================ RESTART: Shell ================================
>>> "0123456789"[2:5:-1]
''
>>> "0123456789"[5:2:-1]
'543'
>>> "0123456789"[:2:-1]
'9876543'
>>> "0123456789"[::-1]
'9876543210'
>>> 
================================ RESTART: Shell ================================
>>> x = "доход"
>>> print(bool(x==x[::-1]))
True
>>> x = "поход"
>>> print(bool(x==x[::-1]))
False
>>> 