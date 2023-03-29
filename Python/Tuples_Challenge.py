Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>>   mytuple = ("air", "water", "dirt")
...   
SyntaxError: unexpected indent
>>> mytuple = ("air", "water", "dirt")
>>> print(tuple)
<class 'tuple'>
>>> print(mytuple)
('air', 'water', 'dirt')
>>> 
>>> 
>>> mytuple = ("air", "water", "dirt")
>>> for x in mytuple:
...     print(x)
... 
...     
air
water
dirt
>>> 
>>> thistuple = (1,3,7,8,7,5,4,6,8,5)
>>> 
>>> x = thistuple.count(5)
>>> 
>>> print(x)
2
