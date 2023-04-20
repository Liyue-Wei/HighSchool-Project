from pytube import YouTube

selection = False
while(selection == False):
    url = YouTube(input("input url : "))
    print(url.title)
    check = input("Y/N : ")
    
    if(check == "Y"):
        selection = True
        print("processing")
        url.streams.get_highest_resolution().download()
        print("finish process")
        selection = False
        
    else:
        del url
        selection = False  
        print("retype url or press any key to break")
        
