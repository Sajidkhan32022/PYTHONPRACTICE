def calculator(x,y,oper):
    if oper == '+' :
        print('sum is equal to =',x + y)
    if oper == '-' :
        print('sub is equal to =',x - y)
    if oper == '*' :
        print('multi is equal to =',x * y)
    if oper == '/' :
        print('div is equal to =',x / y)
    if oper == '%' :
        print('mod is equal to =',x % y)
    if oper == '**' :
        print('suq is equal to =',x ** y)
num1=int(input('num1 = '))
num2=int(input('num2 = '))
oper=(input('oper = '))
calculator(num1,num2,oper) 

       