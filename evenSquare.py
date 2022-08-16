def evenSquare():
    even=[i*i for i in range(21) if i%2==0 and i%3!=0]
    return sum(even)
print(evenSquare())