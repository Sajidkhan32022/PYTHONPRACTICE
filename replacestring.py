txt='sajid khan computer systems engineer'
count=0
for i in (txt):
    if i == 's':
        count+=1
x=len(txt)
print(count)
print(x) 
print(int((count/x)*100),'%')
n=int(input('n = '))
if n%2 == 0 and 5>=n >=2:
    print('Not Weried')
if n%2 == 0 and 20>= n >=6:
    print('Weried')
if n%2 == 0 and n>20:
    print('Not Weried')
if n%2!=0:
    print('Weried')

