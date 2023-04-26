i = int(input())
l = []
a1 = 0
a2 = 0
a3 = 0
for n in range(0, i):
    v = int(input())
    if(v%3==0):
        a1+=1
    elif(v%3==1):
        a2+=1
    elif(v%3==2):
        a3+=1
print("{} {} {}".format(a1, a2, a3))
