class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node
  
    def printt(self):
        print (self.data)
  
class LinkList:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False
      
      
    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
    
        else:
            current_node = self.head
            new_node = Node(data)
            while (current_node.next != None):
                current_node = current_node.next
            current_node.next = new_node
      
    def printt(self):
        array = []
        if self.head == None:
            return array
        else:
            current_node = self.head
            while (current_node.next != None):
                array.append(current_node.data)        
                current_node = current_node.next
        array.append(current_node.data)
        return array

    def getCount(self):
        temp = self.head 
        count = 1 
        while (temp.next):
            count += 1
            temp= temp.next
        return count
      
L = LinkList()
L.insert("x")
L.insert("y")
L.insert("z")
L.insert("1")
L.insert("2")
L.insert(3)

print (L.printt())
print ("Count of nodes is :",
            L.getCount())