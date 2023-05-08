i, n, t = map(int, input().split(' '))
s = (i+n+t)/2
print(int(pow((s*(s-i)*(s-n)*(s-t)), 1)))