while(True):
    i = int(input())
    if(i==0):
        break
    else:
        for n in range(0, i):
            if(n%7==0):
                continue
            else:
                print(n, end=" ")
        print('\n')
                