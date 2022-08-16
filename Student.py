class Student:
    def __init__(self,Name,RollNumber):
        self.__Name = Name
        self.__RollNumber = RollNumber

    def setName(self,Name):
        self.__Name = Name

    def getName(self):
        return (self.__Name) 

    def setRollNumber(self , RollNumber):
        self.__RollNumber = RollNumber

    def getRollNumber(self):
        return self.__RollNumber

student = Student('Rehana' , 25)
#print(student.getName())
#print(student.getRollNumber())
student.setName('sajid')
student.setRollNumber(1554)
print(student.getName())
print(student.getRollNumber())
class Student:
    # defining the properties   
    ID = None
    GPA = None

# creating an object of the Student class
Peter = Student()

# assigning values to properties of Peter
Peter.ID = 3789
Peter.GPA = 3.5

# create a new attribute for Peter
Peter.department = "Computer Science"


# Create another Student object
John = Student()
John.ID = 3790
John.GPA = 3.7


# Printing properties of Peter
print("ID =", Peter.ID)
print("GPA", Peter.GPA)
print("Department:", Peter.department)

# Printing properties of John
print("ID =", John.ID)
print("GPA", John.GPA)
print("Department:", John.department)
