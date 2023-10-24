i = int(input())
l = list(map(int, input().split()))
l.sort()

count_dict = {}

for num in l:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

Max = max(count_dict.values())

for num, count in count_dict.items():
    if count == Max:
        print("{} {}".format(num, Max))

'''
i = int(input())
l = list(map(int, input().split()))
l.sort()
n = []
t = []

for a in range(0, len(l)):
    if(l[a] not in n):
        n.append(l[a])

for a in range(0, len(n)):
    t.append(0)
    for b in range(0, len(l)):
        if(n[a]==l[b]):
            t[a]+=1

Max = max(t)

for a in range(0, len(t)):
    if(t[a]==Max):
        print("{} {}".format(n[a], Max))
'''