from pytube import YouTube

selection = False
while(selection == False):
    url = YouTube(input("input url : "))
    url_streams = url.streams
    url_title = url.title
    print(url_streams)
    print(url_title)
    check = input("Y/N : ")
    
    if(check == "Y"):
        selection = True
        print("processing")
        url_streams.get_highest_resolution().download()
        print("finish process")
        selection = False
        
    else:
        del url
        selection = False  
        print("retype url or press any key to break")
        
