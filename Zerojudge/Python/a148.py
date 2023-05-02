i = []
while(True):
    try:
        i = input().split(' ')
        t = 0
        for n in range(1, len(i)):
            t+=int(i[n])
        if(t/float(i[0])>59):
            print("no")
        else:
            print("yes")
    except:
        break