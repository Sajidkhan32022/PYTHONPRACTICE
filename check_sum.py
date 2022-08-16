def check_sum(y):
    for i in y:
        for j in y:
            if i+j==0:
                return True
    else:
        return False
x=[10, -14, 26, 5, -3, 13, -4]
result=check_sum(x)
print(result)



