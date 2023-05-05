i = int(input())
n = input().split(' ')
l = 0
for t in range(len(n)):
    if(int(n[t])<=10):
        l+=1
print(l)