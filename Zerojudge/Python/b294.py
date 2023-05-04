i = int(input())
n = []
l = []
sum = 0
n = input().split(' ')
for t in range(0, i):
    l.append(t+1)
    sum+=int(n[t])*int(l[t])
print(sum)