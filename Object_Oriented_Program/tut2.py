#  Class And Instance Variables

class Employee:
    increment = 1.5  # it is the variable of class not constructor
    no_of_employee = 0

    def __init__(self, fname, lname, salary):  # constructor
        self.fname = fname
        self.lname = lname
        self.salary = salary        # here it is called the instance variable
        self.increment = 1.4       # here  it is the variable of constructor
        Employee.no_of_employee += 1

    def increase(self):
        self.salary = self.salary * self.increment

# if we write self.increment then the compiler search increment in instance or constructor if there is not present
# of increment then it will serach in the class
# if we write Employee.increment then it will only search the increment variable
# in class because emplyee is the class name.

print(Employee.no_of_employee)
amit = Employee("Amit", "Banerjee", 44000)
rohan = Employee("Rohan", "Singh", 32000)
rajesh = Employee("Rajesh","Kumar",67000)
print(Employee.no_of_employee)
print(Employee.increment)

'''
print(amit,rohan)
print(rohan.lname)
print(amit.salary)'''

print(amit.salary)
amit.increase()
print(amit.salary)
