def findEvenOdd(i):
    e=''
    o=''
    for j in range(len(i)):
        if j%2==0:
            e+=i[j]
        else:
            o+=i[j]
    return e , o
if __name__ == '__main__':
    int1=int(input())
    str1=[]
    for i in range(int1):
        str=input()
        str1.append(str)
    for i in str1:
        odd,even=findEvenOdd(i)
        print(odd,even)
    