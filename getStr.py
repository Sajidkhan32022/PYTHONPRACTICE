def getStr(str1):
    temp = ''
    for i in str1:
        if i !=' ':
            j = i * int(len(str1))
            temp += j
    return temp


print(getStr('abc'))



