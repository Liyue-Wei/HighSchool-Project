i = int(input())
l = input().split(' ')
if(i%2==1):
    print(l[int(i/2)])
else:
    print(int((int(l[int(i/2)])+int(l[int(i/2)-1]))/2))