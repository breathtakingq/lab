Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> my_list = ["победа","ничья", "поражение"]
>>> type(my_list)
<class 'list'>
>>> len(my_list)
3
>>> my_list[1]
'ничья'
>>> id(my_list[0])
2391839793536
>>> id(my_list[1])
2391839882576
>>> id(my_list[2])
2391840467856
>>> my_list[]
SyntaxError: invalid syntax
>>> my_list = []
>>> type(my_list)
<class 'list'>
>>> len(my_list)
0
>>> my_list = []
>>> 'не пустой' if my_list else 'пустой'
'пустой'
>>> my_list = [[], []]
>>> type(my_list)
<class 'list'>
>>> len(my_list)
2
>>> 