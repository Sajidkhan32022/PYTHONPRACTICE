class Employee:
    def __init__(self,Name,ID,dep):
        self.__Name = Name
        self.__ID = ID
        self.__dep = dep

    def getName(self):
        return self.__Name

    def setName(self,Name):
        self.__Name = Name

    def getID(self):
        return self.__ID

    def setID(self,ID):
        self.__ID = ID
    def getdep(self):
        return self.__dep

    def setdep(self,dep):
        self.__dep= dep

obj1=Employee('sajid',1554,'cse')
print(obj1.getName())
print(obj1.getID())
print(obj1.getdep())

obj1.setName('Rehana')
obj1.setID(25)
obj1.setdep('isl')

print(obj1.getName())
print(obj1.getID())
print(obj1.getdep())






