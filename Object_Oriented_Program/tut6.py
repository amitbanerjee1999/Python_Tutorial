# Inheritence in oops

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
    def change_Increment(cls, amount):      # alternative constructor to  make change with class variable
        cls.increment = amount

    @classmethod                    # alternative constructor to  make change with class variable
    def from_str(cls, emp_string):
        fname, lname, salary = emp_string.split("-")
        return cls(fname, lname, salary)

    @staticmethod                   # Normal method function using decorator
    def isOpen(day):
        if(day == "Sunday"):
            return False
        else:
            return True


class Programmer(Employee):
    def __init__(self, fname, lname, salary, proglang, exp):
        super().__init__(fname, lname, salary)
        self.proglang = proglang
        self.exp = exp

    def increase(self):
        self.salary = (self.salary * (self.increment+0.2))
        return self.salary

manish = Programmer("Manish", "Paul", 99000, "JAVA", "5 yrs")
print(manish.exp)
# help(Programmer)
print(manish.salary)
manish.change_Increment(3)
print(manish.increase())
print(manish.salary)


# amit = Employee("Amit", "Banerjee", 44000)
# ravi = Employee.from_str("Ravi-Kumar-75000")
# rohan = Employee("Rohan", "Singh", 32000)
#
#
# print(ravi.fname)
# print(amit.salary)
# print(rohan.lname)