int1=int(input())
str1=[]
for i in range(int1):
    str=input()
    str1.append(str)
for i in str1:
    e=''
    o=''
    for j in range(len(i)):
        if j%2==0:
            e+=i[j]
        else:
            o+=i[j]
    print(f'{e} {o}')
