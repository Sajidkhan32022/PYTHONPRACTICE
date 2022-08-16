def sublist(l2):
    subl1=[]
    subl2=[]
    subl3=[]
    for i in l2:
        if i == 1 or i == 4 or i == 7:
            subl1.append(i)
        if i == 2 or i == 5 or i == 8:
            subl2.append(i)
        if i == 3 or i == 6 or i == 9:
            subl3.append(i)
    return subl1 ,subl2,subl3 
        

l1=[1,2,3,4,5,6,7,8,9]
print(sublist(l1))