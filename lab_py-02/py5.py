Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> (1-2j)*(1+3j)
(7+1j)
>>> (1-2j)/(1+3j)
(-0.5-0.49999999999999994j)
>>> (1-2j)//(1+3j)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    (1-2j)//(1+3j)
TypeError: can't take floor of complex number.
>>> (1-2j)%(1+3j)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    (1-2j)%(1+3j)
TypeError: can't mod complex numbers.
>>> (1-2j)**2
(-3-4j)
>>> (1-2j)**2.1
(-3.7104784958643933-3.9494079187807873j)
>>> (1-2j)**(1+3j)
(16.150190764018866+59.7973809362117j)
>>> 
================================ RESTART: Shell ================================
>>> (3-4j).conjugate()
(3+4j)
>>> (3-4j)*(3+4j)
(25+0j)
>>> (25+oj)**0.5
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    (25+oj)**0.5
NameError: name 'oj' is not defined
>>> (25+0j)**0.5
(5+0j)
>>> (5+0j).real
5.0
>>> abs(3-4j)
5.0
>>> complex(3)
(3+0j)
>>> 