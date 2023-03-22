from pytube import YouTube
import tkinter as tk
import ttkbootstrap as ttk
import os

win = ttk.Window(themename="darkly")
win.geometry("1280x720")
win.title("YouTube Downloader")
win.resizable(0, 0)

def path():
    file_path = os.path.abspath(os.path.dirname(__file__))
    file_path = file_path.replace("\\", "/")
    length = len(file_path)
    file_path_2 = []
    for i in range(0, length):          
        file_path_2.append(file_path[i])

    return (file_path_2)

def path_function(direct_path):
    file_path = path()
    file_path.append(direct_path)
    file_path = "".join(file_path)
    return(file_path)

class GUI_interface:
    ttk.Label(win, text="YouTube Downloader", font=("微軟正黑體", 20)).place(x=10, y=10)
    ttk.Label(win, text="輸入影片網址", font=("微軟正黑體", 14)).place(x=10, y=90)
    ttk.Entry(win, font=("微軟正黑體", 16), width=57).place(x=10, y=135)
    tk.Button(win, text="Search", font=("微軟正黑體", 13)).place(x=1116, y=135, width=154, height=184)
    ttk.Label(win, text="下載位置 (預設為下載)", font=("微軟正黑體", 14)).place(x=10, y=220)
    ttk.Entry(win, font=("微軟正黑體", 16), width=57).place(x=10, y=265)
    ttk.Label(win, text="影片資訊", font=("微軟正黑體", 14)).place(x=10, y=350)
    ttk.Frame(win, height=5, width=1260, style="darkly").place(x=10, y=395)
    tk.Button(win, text="Download", font=("微軟正黑體", 13)).place(x=1116, y=415, width=154, height=294)

    win.mainloop()