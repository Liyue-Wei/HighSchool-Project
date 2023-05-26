i, n = map(int, input().split(' '))
if(n==0 or i%n==0):
    print("OK!")
else:
    print(i%n)