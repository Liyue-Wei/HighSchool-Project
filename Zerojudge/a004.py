while(i:=input()):
    if(i=="EOF"):
        break
    if(int(i)%4==0 and int(i)&100!=0):
        print("閏年")
    elif(int(i)&400==0):
        print("閏年")
    else:
        print("平年")