def rec_count(number):
    print(number)
    # Base case
    if number == 0:
        return 0
    rec_count(number - 1)  # A recursive call with a different argument
    print(number)


rec_count(5)
print('sjid khn')
A = [1, 4, 9]
s = ''.join(map(str, A))
print(s)
#print(int(s) + 1)
for i in reversed(range(1, len(A))):
    print(A[i])