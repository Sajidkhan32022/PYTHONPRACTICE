class Animal:
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound

    def Animal_details(self):

        print('Name :',self.name ,'\n''Sound :',self.sound)


class Dog(Animal):

    def __init__(self,name,sound,family):
        self.family = family
        super().__init__(name,sound)

    def Animal_details(self):

        print('Name :',self.name ,'\n' 'Sound :',self.sound , '\n' 'family : ', self.family)

class Sheep(Animal):

    def __init__(self,name,sound,color):
        self.color = color
        super().__init__(name,sound)

    def Animal_details(self):

        print('Name :',self.name ,'\n' 'Sound :',self.sound , '\n' 'family : ', self.color)







obj1 = Dog('dog','Woof Woof',"Husky") 
obj1.Animal_details()

print('')

s = Sheep("Billy", "Baaa Baaa", "White")
s.Animal_details()

    



