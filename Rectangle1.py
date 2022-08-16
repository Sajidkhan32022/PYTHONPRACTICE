class Rectangle1:
    def __init__(self,x1,y1,x2,y2):
            self.x1=x1
            self.x2=x2
            self.y1=y1
            self.y2=y2
        
            
    def coordinate(self):
        return (self.x1,self.y1),(self.x2,self.y2)

    def width(self):
        return self.y2-self.y1

    def height(self):
        return self.x2-self.x1

    def area(self):
        return  self.width() * self.height()

    def perimeter(self):
        return  2*self.height() + 2*self.width()


class Square(Rectangle1):
    def __init__(self,x1,y1,length):
        x2 = x1 + length
        y2 = y1 + length
        super().__init__(x1,y1,x2,y2)

    def area(self):
        return super(). area()

    def width(self):
        return super(). width()

    


    
    
    
    
'''obj = Rectangle1(2,7,5,3)
print(obj.coordinate())
print(obj.height())
print(obj.width())
print(obj.area())
print(obj.perimeter())'''
square = Square (2, 7, 7)
print('Area = ',square.area())
print('lenght = ',square.width())

