i = []
while(True):
    try:
        n = input()
        if(n in i):
            print("YES")
        else:
            print("NO")
            i.append(n)
    except:
        break