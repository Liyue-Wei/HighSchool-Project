n = int(input())
t = sorted([int(x) for x in input().split()])
print(*t)
BC = -1
WC = 101
for i in t:
    if i<60 and i>BC:BC=i
    elif i>=60 and i<WC:WC=i
if BC==-1:
    print("best case")
else:
    print(BC)
if WC==101:
    print("worst case")
else:
    print(WC)