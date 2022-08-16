class Circle:
    def __init__(self,radius):
        self.radius=radius

    def print_area(self):
        return (3.14*(self.radius**2))
obj = Circle(3)
print(obj.print_area())
class Employee:

    def __init__(self, name='', ID=0, department=''):

        # Declare the attributes here
        self.__name=name
        self.__ID=ID
        self.__department=department

    def get_name(self,name):
        return self.__name
    def set_name(self,name):
        self.name=name
    def get_ID(self,ID):
        return self.__ID
