i = str(input())
n = []
for t in range(len(i)):
    try:
        n.append(ord(i[t]))
    except:
        break
for l in range(len(n)):
    if(l==len(n)-1):
        print("{}".format(n[l]), end="")
    else:
        print("{}_".format(n[l]), end="")


