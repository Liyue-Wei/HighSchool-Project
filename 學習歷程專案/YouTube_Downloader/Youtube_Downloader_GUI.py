from pytube import YouTube

def get_youtube():
    selection = False
    while(selection == False):
        url = YouTube(input("input url : "))
        print(url.title)
        check = input("Y/N : ")
   
        if(check == "Y"):
            selection = True
            print("processing")
            url.streams.first().download()
            print("finish process")
        
        else:
            del url
            selection = False  
            print("retype url or press any key to break")
        
import tkinter as tk

win = tk.Tk()
win.geometry("720x480")
win.resizable(0, 0)
win.title("Youtube Downloader")

class GUI_interface():
    global url_input
    url_input = tk.StringVar()
    label1 = tk.Label(win, text="Download Youtube Films Here", font=("微軟正黑體", 24), fg="black")
    label1.pack()
    label2 = tk.Label(win, text="Input URL", font=("微軟正黑體", 18), fg="gray")
    label2.pack()
    input_url = tk.Entry(win, font=("微軟正黑體", 20), textvariable=url_input)
    input_url.pack()

win.mainloop()