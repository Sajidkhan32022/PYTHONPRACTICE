l=[10,20,71,40,50,39,800,9008]
max=10
for i in range(len(l)):
    if l[i] > max :
        max=l[i]
        index=i
print(f'max is {max} and its index is {index}')