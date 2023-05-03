a, b, c = map(str, input().split(" "))
a, c = int(a), int(c)
if(b=="+"):
    print(int(a+c))
if(b=="-"):
    print(int(a-c))
if(b=="*"):
    print(int(a*c))
if(b=="/"):
    print(int(a/c))