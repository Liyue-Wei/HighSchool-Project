'''
while True:
    s, e, b, k = map(int, input().split(' '))
    i, n = s, s
    list_1 = []    #b倍數
    list_2 = []    #b+10
    while(i<=e):
        if(s<=b):
            list_1.append(b)
            s+=b
        else:
            list_1.append(s+b)
            s+=b
    print(list_1)
'''

while True:
    s, e, b, k = map(int, input().split(' '))
    n = 1
    for i in range(s, e):
        if(i%b==0 or i%10==b):
            n+=1
        if n==k:           
            break
    print(n)