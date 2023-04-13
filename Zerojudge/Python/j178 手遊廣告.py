i, n = map(int, input().split(' '))
t = list(map(int, input().split(' ')))
for a in range(0, i):
    if(n>t[a]):
        n+=t[a]
    else:
        break
print(n)
