class Stack:
    def __init__(self):
        self.items=[]
    
    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items

    def sizee(self):
        temp=self.items
        count=0

        for i in range(len(temp)):
            count+=1
    
        return count 
        




my_stack = Stack()
my_stack.push('A')
my_stack.push('B')
my_stack.push('C')
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
#print(my_stack.sizee())


