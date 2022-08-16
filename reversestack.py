class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
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

    def reverse_string(self):
        #for i in range(len(self.items)):
            #self.push(self.items[i])
        rev_str = ""
        while not self.is_empty():
            rev_str += self.pop()

        return int(rev_str)

stack = Stack()
stack.push('1')
stack.push('2')
stack.push('3')
print(stack.reverse_string())
''' from stack import Stack
def reverse_string(stack, input_str):
  for i in range(len(input_str)):
    stack.push(input_str[i])
  rev_str = ""
  while not stack.is_empty():
    rev_str += stack.pop()

  return rev_str

stack = Stack()
input_str = "!evitacudE ot emocleW"
print(reverse_string(stack, input_str)) '''



    