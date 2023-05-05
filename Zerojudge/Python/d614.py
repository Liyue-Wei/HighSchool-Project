i = int(input())
while(i>0):
    n = input().split(' + ')
    l = 0
    for t in range(len(n)):
        l+=int(n[t])
    print(l)
    i-=1