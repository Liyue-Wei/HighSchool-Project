while(True):
    try:
        i, n = map(int, input().split(' '))
        print(abs(i-n))
    except:
        break