class Employee:
    # defining the initializer
    def __init__(self, ID=None, salary=None, department=None):
        self.ID = ID
        self.salary = salary
        self.department = department

    def tax(self):

        return (self.salary * 0.2)

    def salaryPerDay(self):
        return (self.salary / 30)


# initializing an object of the Employee class
Steve = Employee(3789, 2500, "Human Resources")
# Printing properties of Steve
print("ID =", Steve.ID)
print("Salary", Steve.salary)
print("Department:", Steve.department)
print("Tax paid by Steve:", Steve.tax())
print("Salary per day of Steve", Steve.salaryPerDay())
class Student:
    def __init__(self,name,pyh,chem,bio):
        self.name=name
        self.pyh=pyh
        self.chem=chem
        self.bio=bio
    

    def totalObtained(self):
        
        return  (self.pyh + self.chem + self.bio)

    def percentage(self):
        return  ((self.totalObtained()/300)*100)
         

        
demo1= Student('Mark',80,90,40)
print(demo1.name)
print(demo1.totalObtained())
print(demo1.percentage ())