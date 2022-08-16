def dollars(d):
    D_L=[0.25,0.10,0.05,0.01]
    C_L=[]
    for i in D_L:
        x=d//i
        C_L.append(x)
        d=d%i
    return C_L

print(dollars(2.24))
print(dollars(2.24))
print(dollars(1.19))
print(dollars(4.16))



