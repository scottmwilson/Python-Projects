Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> animal = ( 'zebra', 'alligator', 'giraffe', 'goat', 'ox' )
>>> 
>>> listofAnimals.append ("honey badger")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    listofAnimals.append ("honey badger")
NameError: name 'listofAnimals' is not defined
>>> listofAnimals = list(animal)
>>> print(listofAnimals)
['zebra', 'alligator', 'giraffe', 'goat', 'ox']
>>> 
>>> listofAnimals.append("honey badger")
>>> print(listofAnimals)
['zebra', 'alligator', 'giraffe', 'goat', 'ox', 'honey badger']
>>> 
>>> myString = "Hello! I am please to meet you"
>>> newString = list(myString)
>>> print(newString)
['H', 'e', 'l', 'l', 'o', '!', ' ', 'I', ' ', 'a', 'm', ' ', 'p', 'l', 'e', 'a', 's', 'e', ' ', 't', 'o', ' ', 'm', 'e', 'e', 't', ' ', 'y', 'o', 'u']
>>> 
>>> newString = myString.split(" ")
>>> print(newString)
['Hello!', 'I', 'am', 'please', 'to', 'meet', 'you']
