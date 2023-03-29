Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> answer = True
>>> 
>>> type(answer)
<class 'bool'>
>>> answer = False
>>> type(answer)
<class 'bool'>
>>> 
>>> a = 500
>>> b = 66
>>> 
>>> if b > a:
...     print("b is greater than a")
... else:
...     print("bi is not greater than a")
... 
bi is not greater than a
>>> 
>>> print(bool("abc"))
True
>>> print(bool(123))
True
>>> print(bool(["apple", "cherry", "banana"]))
True
