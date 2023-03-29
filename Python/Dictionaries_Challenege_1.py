Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year" : 1964
}
print(thedict)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(thedict)
NameError: name 'thedict' is not defined. Did you mean: 'thisdict'?
>>> print(thisdict)
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
>>> 
>>> thisdict = {
...     "brand": "Ford",
...     "model": "Mustang",
...     "year" : 1964
... }
>>> 
>>> x = thisdict.get("model")
>>> print(x)
Mustang
>>> 
>>> thisdict = {
...     "brand": "Ford",
...     "model": "Mustang",
...     "year" : 1964
... }
>>> thisdict["year"] = 2018
>>> print(thisdict)
{'brand': 'Ford', 'model': 'Mustang', 'year': 2018}
>>> 
>>> thisdict = {
...     "brand": "Ford",
...     "model": "Mustang",
...     "year" : 1964
... }
>>> thisdict["color"] = "red"
>>> print(thisdict)
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}
>>> 
>>> myfamily = {
...     "Child1" : {
...     "name" : "Emil",
...     "year" : 2004
...     },
...     "Child2" : {
...     "name" : "Tobias",
...     "year" : 2011
...     },
...     "Child3" : {
...     "name" : "Linus",
...     "year" : 2011
...     }
... }
>>> 
>>> print(myfamily)
{'Child1': {'name': 'Emil', 'year': 2004}, 'Child2': {'name': 'Tobias', 'year': 2011}, 'Child3': {'name': 'Linus', 'year': 2011}}
>>> 
>>> 
>>> x= ('key1', 'key2', 'key3')
>>> y= 0
>>> 
>>> thisdict = dict.fromkeys(x, y)
>>> 
>>> print(thisdict)
{'key1': 0, 'key2': 0, 'key3': 0}
