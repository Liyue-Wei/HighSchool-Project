a = int(input())
while(a>0):
    i = input()
    n = len(i)
    l = 1
    for t in range(n):
        l*=int(i[t])
    print(l)
    a-=1
