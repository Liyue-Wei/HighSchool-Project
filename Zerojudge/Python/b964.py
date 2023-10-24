i = int(input())
n = list(map(int, input().split(' ')))
n.sort()
T = []
F = []
(Max, Min) = (max(n), min(n))
(worst, best) = (0, 0)

for t in range(0, i):
    if(n[t]>=60):
        T.append(n[t])

    else:
        F.append(n[t])

for t in range(0, i):
    print(n[t], end=' ')

if(len(T)!=0 and len(F)!=0):
    print('\n{}\n{}'.format(F[-1], T[0]))
    
else:
    print('\n{}\n{}'.format(F[-1], "worst case")) if(len(T)==0) else print('\n{}\n{}'.format("best case", T[0]))
    