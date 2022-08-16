def diagonalDifference(arr):
    left_to_right_dia = 0
    right_to_left_dia = 0
    for i in range(len(arr)):
        left_to_right_dia+=arr[i][i]
        right_to_left_dia+=arr[i][len(arr)-i-1]
    return abs(left_to_right_dia - right_to_left_dia)
arr=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
result = diagonalDifference(arr)

print(result)
