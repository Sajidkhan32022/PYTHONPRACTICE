def inRange(x,y,num):
    if y < num < x :
        return f'num {num} is in range between {x} and {y} '
    else:    
        return f'num {num} is not in range between {x} and {y}'
x = int(input(' x = '))
y = int(input(' y = '))
num=int(input(' num = '))
print(inRange(x,y,num))