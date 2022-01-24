#   class method as an alternative constructor

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
    def change_Increment(cls, amount):      # class method constructor
        cls.increment = amount

    @classmethod                    # alternative constructor
    def from_str(cls, emp_string):
        fname, lname, salary = emp_string.split("-")
        return cls(fname, lname, salary)

amit = Employee("Amit", "Banerjee", 44000)
ravi = Employee.from_str("Ravi-Kumar-75000")
rohan = Employee("Rohan", "Singh", 32000)


print(ravi.fname)