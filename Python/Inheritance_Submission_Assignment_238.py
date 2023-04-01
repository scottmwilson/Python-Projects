
#This is a new class
class User:
    name = 'Mom'
    email = 'mom@gmail.com'
    password = 'Xmdu#4fi%9?'
    account_number = 1

#This is a child class
class Employee(User):
    base_pay = 150000.00
    department = 'Product Development'

#This is a child class
class Customer(User):
    email_address = 'mrbig@yahoo.com'
    mailing_list = True 
