while(i:=input()):
    if(int(i)%4==0 and int(i)&100!=0):
        print("閏年")
    elif(int(i)&400==0):
        print("閏年")
    else:
        print("平年")

'''
不知道為何一直RE，可能是break不掉的關係
'''