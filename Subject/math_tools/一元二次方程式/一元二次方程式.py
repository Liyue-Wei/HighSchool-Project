global a,b,c,x,y,d 
a, b, c = map(float, input().split())
    
d = int(((b**2)-(4*a*c)))
x = int((-b/(2*a)))
y = int((((4*a*c)-b**2)/4*a))
print(d)

        
if(d < 0):
    print('\a', "無實根", '\n', "頂點 ", x, ",", y, '\n')

if(d == 0):
     print("重根 x=", ((-b)+d**(1/2))/(2*a), '\n')
     print("頂點 ", x, ",", y, '\n')

if(d > 0):
    print("x1=", ((-b)+d**(1/2))/(2*a), '\n')
    print("x2=", ((-b)-d**(1/2))/(2*a), '\n')
    print("頂點 ", x, ",", y, '\n')

print("以降冪排列輸入係數")