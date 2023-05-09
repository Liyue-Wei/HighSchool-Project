import re
while(True):
    try:
        b = str(input())
        t = b
        a = []
        for l in range(len(t)):
            if(t[l]=="." or t[l]=="!" or t[l]=="?"):
                a.append(t[l])
        b = re.split('\. |\! |\? |\!|\ i', b)
        if(len(b)!=1):
            b.pop()
            for n in range(len(b)):
                spl = str(b[n]).capitalize()
                print("{}{}".format(spl, a[n]), end=' ')
            print('\n')
        else:
            for n in range(len(b)):
                spl = str(b[n]).capitalize()
                print(spl, end=' ')
            print('\n')
    except:
        break
