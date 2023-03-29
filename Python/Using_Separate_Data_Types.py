Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> num1 = 1
>>> num2 = 2
>>> 
>>> 
>>> print(num1 + num2)
3
>>> num1 = 1.2
>>> num2 = 2.1
>>> print(num1 + num2)
3.3
>>> num1 = "one"
>>> print(num1 + num2)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print(num1 + num2)
TypeError: can only concatenate str (not "float") to str
>>> num1 = "1"
>>> print(num1 + num2)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print(num1 + num2)
TypeError: can only concatenate str (not "float") to str
>>> print(int(num1) + num2)
3.1
