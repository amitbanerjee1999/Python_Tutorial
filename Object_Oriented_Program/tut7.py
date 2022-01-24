# Magic/Dunders Method in python

class Employee:
    increment = 1.5
    no_of_employee = 0

    def __init__(self, fname, lname, salary):  # original constructor
        self.fname = fname
        self.lname = lname
        self.salary = salary

        Employee.no_of_employee += 1

    def increase(self):
        self.salary = self.salary * self.increment

    @classmethod
    def change_Increment(cls, amount):  # alternative constructor to  make change with class variable
        cls.increment = amount

    @classmethod  # alternative constructor to  make change with class variable
    def from_str(cls, emp_string):
        fname, lname, salary = emp_string.split("-")
        return cls(fname, lname, salary)

    @staticmethod  # Normal method function using decorator
    def isOpen(day):
        if (day == "Sunday"):
            return False
        else:
            return True

    def __add__(self,other):        # Dunder
        return self.salary + other.salary


    def __repr__(self):             # Dunder
        return 'Employee({}, {}, {})'.format(self.fname, self.lname, self.salary)


    def __str__(self):              # Dunder
        return 'The name of the Employee is : {}'.format(self.fname)


amit = Employee("amit", "roy", 900000)
rohan = Employee("Rohon", "Meheta", 9)

print(amit+rohan)
print(repr(amit))
print(str(amit))

# a = 6
# print(a.__add__(7))   # Dunder

# a = 6
# print(a.__mul__(7))