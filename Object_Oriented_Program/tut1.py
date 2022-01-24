# Class and Object

class Employee:
    def __init__(self, fname, lname, salary):           # constructor
        self.fname = fname
        self.lname = lname
        self.salary = salary


amit = Employee("Amit", "Banerjee", "44000")
rohan = Employee("Rohan", "Singh", "32000")
'''
// First we made class of Rohan and Amit.
// here amit and rohan is an object 

amit.fname = "Amit"
amit.lname = "Banerjee"
amit.salary = 44000

rohan.fname = "Rohan"
rohan.lname = "Singh"
rohan.salary = "32000"

print(rohan,harry)      // it only gives the address

'''
print(amit,rohan)
print(rohan.lname)
print(amit.salary)