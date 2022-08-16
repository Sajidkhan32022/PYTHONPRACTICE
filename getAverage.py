def getAverage(L):
    count=0
    sum=0
    for i in L:
        sum+=i
        count+=1
    return sum/count
print(getAverage([1,4,9,10,23]))