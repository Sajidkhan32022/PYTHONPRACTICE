def checkParity(num):
    if num%2 == 0 :
        return 'number is even'
    else:
        return  'number is odd'
x=int(input(' x = '))
E_O=checkParity(x)
print(E_O)