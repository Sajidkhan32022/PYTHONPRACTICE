class Item:
    def __init__(self,name,price):
        self.name=name
        self.price=price


class  ShoppingCart:
    def __init__(self):
        self.item=[]
    
    def add(self,item):
        self.item.append(item)
    
    def print(self):
        for i in self.item:
            print(i.name)

    def total(self):
        sum = 0
        for i in self.item:
            sum+=i.price
        print(sum)

    def len(self):
        print(len(self.item))


item1 = Item('bike',120000)
item2 = Item('cycle',25000)
item3 = Item('car',3500000)
item4 = Item('moble',50000)


cart = ShoppingCart()
cart.len()
cart.add(item1)
cart.len()
cart.total()
cart.add(item2)
cart.add(item3)
cart.add(item4)
cart.len()
#cart.print()
cart.total()

    

