#  Class And Method Variables

class Employee:
    increment = 1.5  # it is the variable of class not constructor
    no_of_employee = 0

    def __init__(self, fname, lname, salary):  # constructor
        self.fname = fname
        self.lname = lname
        self.salary = salary
        Employee.no_of_employee += 1

    def increase(self):
        self.salary = self.salary * self.increment

    # to run a method which is dependent on class but not with instance then we have to implement class method decorator
    @classmethod
    def change_Increment(cls, amount):
        cls.increment = amount

amit = Employee("Amit", "Banerjee", 44000)
rohan = Employee("Rohan", "Singh", 72000)

print(amit.salary)
Employee.change_Increment(2)
amit.increase()
print(amit.salary)


