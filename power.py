L = [1,2,4,8,16,32,64]
x = 5
found = False
i = 0
while not found and i<len(L):
    if 2**x == L[i]:
        found = True
    else:
        i = i+1

if found:
    print('at index',i)
else:
    print(x,'not found')
