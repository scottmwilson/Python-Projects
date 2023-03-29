Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
...  
>>> myset = ["apple", "banana", "cherry"}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> myset = {"apple", "banana", "cherry"}
>>> print(myset)
{'banana', 'apple', 'cherry'}
>>> 
>>> myset = {"apple", "banana", "cherry"}
>>> myset.remove("banana")
>>> 
>>> print(myset)
{'apple', 'cherry'}
>>> 
>>> x = {"buildings", "houses", "apartments"}
>>> y = {"google", "microsoft", "apple"}
>>> 
>>> z = x.difference(y)
>>> 
>>> print(z)
{'apartments', 'houses', 'buildings'}
