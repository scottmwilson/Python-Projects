Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> myString = "hello world"
>>> myString
'hello world'
>>> len(myString)
11
>>> myString[0]
'h'
>>> myString[1]
'e'
>>> fName = "SCott"
>>> lName = "Wilson"
>>> print(fName + lName)
SCottWilson
>>> 
>>> print(fName + " " lName)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print(fName + " " + lName)
SCott Wilson
>>> print("Hello {} {}, welcome to Python!".format(fName, lName) )
Hello SCott Wilson, welcome to Python!
