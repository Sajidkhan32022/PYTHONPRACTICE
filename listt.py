def find_max(lst):
    s = None
    for x in lst:
        tempSum = 0
        for y in x:
            tempSum += y
        if(s == None):
            s = tempSum
        elif(s < tempSum):
            s = tempSum
    count = 0
    for x in lst:
        tempSum = 0
        for y in x:
            tempSum += y
        if(s == tempSum):
            count += 1
    return count

#Testing
print(find_max([[1, 2, 3], [2, 3, 5], [10,20,52]])) 


