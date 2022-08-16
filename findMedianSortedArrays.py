from itertools import count


nums1=[1,2,3,4,5]
nums2=[6,7]
merged = nums1 + nums2
count = 0
for i in merged:
    count+=1
if count%2 == 0:
    m=merged[(count//2)-1] + merged [count // 2]
    print(m/2)
else:
    m=merged[count // 2]
    print(m)

    