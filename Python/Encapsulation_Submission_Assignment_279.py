

class Employee:
    def __init__(self, name, salary):
        self._name = name    # protected attribute
        self.__salary = salary    # private attribute
    
    # protected method
    def _calculate_tax(self):
        tax = self.__salary * 0.2
        return tax
    
    # public method to access private attribute and protected method
    def get_net_salary(self):
        tax = self._calculate_tax()
        net_salary = self.__salary - tax
        return net_salary

# create an object that uses protected and private
employee = Employee("John", 5000)
print(employee.get_net_salary())    # output: 4000.0
