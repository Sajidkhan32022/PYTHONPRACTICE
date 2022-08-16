def div_9(n):
    number = str(n)
    counter = 0
    for i in number:
        counter += int(i)
    
    if (counter > 9):
        return div_9(counter)
        
    if (counter == 0 or counter ==9):
        return True
    else:
        return False
    

if __name__=="__main__":
    x=[99,0,18273645,22]

    for i in x:
        print(div_9(i))
        