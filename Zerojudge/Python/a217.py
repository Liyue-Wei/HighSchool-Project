import re
i = str(input())
i = re.split('\,|\.|\!|\?', i)
for n in range(len(i)):
    spl = str(i[n]).capitalize()
    print(spl, end='')
    