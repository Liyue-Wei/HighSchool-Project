i = []
i = str(input().split(""))
for n in range(len(i)/2):
    if(i[n]==i[-1*n]):
        print("yes")
    else:
        print("no")