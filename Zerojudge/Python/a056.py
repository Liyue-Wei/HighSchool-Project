i = int(input())
l = []
y = 0
a = 1
for x in range(0, 1000):
    l.append(x**2)
while(i>0):
    n = int(input())
    t = int(input())
    for z in range(n, t):
        if(z in l):
            y+=z
    print("Case {}: {}".format(a, y))
    i-=1
    a+=1
    n=t=y=0