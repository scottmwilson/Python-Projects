Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> myDictionary = {'index': 1, 'index2':2, 'index3': 355}
>>> myDictionary
{'index': 1, 'index2': 2, 'index3': 355}
>>> myDictionary['index2']
2
>>> dic_users = {'em_1234': {'fname': 'Bob', 'lname': 'Smith', 'phone': '123-456-7890'}, 'em_1235': {'fname': 'Mary', 'lname': 'Jones', 'phone': '152-364-5764'} }
>>> print(dic_users['em_1235']['phone'])
152-364-5764
>>> print('User: {} {}\nPhone: {}'.format(dic_users['em_1235']['fname'],dic_users['em_1235']['lname'], dic_users['em_1235']['phone']))
User: Mary Jones
Phone: 152-364-5764
