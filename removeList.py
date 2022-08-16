def removeList(L):
    updated=[]
    for i in L:
        if i == 4 or i ==9:
            continue
        updated.append(i)
    return updated

print(removeList([1,4,9,10,23]))