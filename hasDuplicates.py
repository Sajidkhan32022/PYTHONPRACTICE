from sys import flags


li=[1,2,3,4,5,7,7]
for i in range(len(li)-1):
    flag=0
    for j in range(i+1,len(li)):
        if li[i]==li[j]:
            flag=1
if flag==1:
    print('has Duplicates')
