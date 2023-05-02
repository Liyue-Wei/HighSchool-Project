i = []
while(True):
    try:
        i = input().split(' ')
        t = 0
        for n in range(1, len(i)):
            t+=int(i[n])
        if(t/int(i[0])>=60):
            print("no")
        else:
            print("yes")
    except:
        break