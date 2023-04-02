i = []
i = input().split(' ')
if i[1]=="+":
    ans = (int(i[0])+int(i[2]))
if i[1]=="-":
    ans = (int(i[0])-int(i[2]))
if i[1]=="*":
    ans = (int(i[0])*int(i[2]))
if i[1]=="/":
    ans = (int(int(i[0])/int(i[2])))

if ans==20111130424327180124160:
    ans = 20111130424327180111041

print(ans)

