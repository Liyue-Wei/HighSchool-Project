i = str(input())
n = []
for t in range(len(i)):
    try:
        n.append(abs(ord(i[t+1])-ord(i[t])))
    except:
        break
for l in range(len(n)):
    print(n[l], end="")


