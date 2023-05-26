l = []
ans = []
for i in range(1, 101):
    l.append(i**2)
    ans.append(sum(l))
while(True):
    try:
        n = int(input())
        if(n!=0):
            print(ans[n-1])
        else:
            break
    except:
        break