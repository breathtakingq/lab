Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> decimal_number = 200
>>> hex_number = hex(decimal_number)
>>> print(hex_number)
0xc8
>>> hex_number = 'c8'
>>> decimal_number = int(hex_number, 16)
>>> print(decimal_number)
200
>>> decimal_number = 200
>>> binary_number = bin(decimal_number)
>>> print(binary_number)
0b11001000
>>> binary_number = '0b11001000'
>>> decimal_number = int(binary_number, 2)
>>> print(decimal_number)
200
>>> decimal_number = 200
>>> octal_number = oct(decimal_number)
>>> print(octal_number)
0o310
>>> 
================================ RESTART: Shell ================================
>>> type(1000000)
<class 'int'>
>>> type (1e6)
<class 'float'>
>>> 