i, n = map(int, input().split(' '))
l=0
if(i%2!=0):
    i+=1
for t in range(i, n+1, 2):
    if(t%2==0):
        l+=1
print(l)

'''
l = 0
for t in range(i, n+1):
    if(t%2==0):
        l+=1
print(l)
'''