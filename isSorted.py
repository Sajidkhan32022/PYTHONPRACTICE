
l1=[9,8,7,6,5,4,3,2,1]
flag=0
for i in range(len(l1)-1):
        if l1[i] < l1[i+1]:
            flag=1
        
if flag==0:
    print("sorted")
else:
    print("not sorted")
'''
def isSorted(list):
  flag = 0
  i = 1
  while i < len(list): 
      if(list[i] < list[i - 1]): # compare with the previous element
          flag = 1
      i += 1
      
  if (not flag) : 
      return True 
  else : 
      return False 
print(isSorted([1,2,3,4,5]))
print(isSorted([1,2,5,4,2])) 
'''
        
        





    
