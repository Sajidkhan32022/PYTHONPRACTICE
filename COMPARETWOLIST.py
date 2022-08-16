ali=[17,28,30] #17 28 30
#99 16 8
khan=[99,16,8]
ali_point=0
khan_point=0
for i in range(len(ali)):
    if ali[i] > khan[i]:
        ali_point+=1
    elif ali[i] < khan[i]:
        khan_point+=1
print([ali_point,khan_point])

