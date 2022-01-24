# Property Decorators Setters & Deleters

class Employee:
    increment = 1.5
    no_of_employee = 0

    def __init__(self, fname, lname, salary):  # original constructor
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.email = fname + lname + '@email.com'

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


if __name__ == '_main__':
    harry = Employee('harry', 'jackson', 99000)
    rohan = Employee('Rohan', 'Agarwal', 9)
    print(harry.email, rohan.email)
