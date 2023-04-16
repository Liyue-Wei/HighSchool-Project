while True:
    s, e, b, k = map(int, input().split(' '))
    i = 0
    for n in range(s, e+1):
        if(n%10==b or n%b==0 or int((n%100)/10)==b):
            i+=1
        if(i==k):
            break
    if(i<k):
        print(-1)
    else:
        print(n)
