from pytube import YouTube
import tkinter as tk
import ttkbootstrap as ttk
import os

win = ttk.Window(themename="darkly")
win.geometry("1280x720")
win.title("YouTube Downloader")
win.resizable(0, 0)

default = "Auto"
resolution = tk.StringVar()
resolution.set(default)

def res_set():
    global res_get
    res_get = resolution.get()
    print(res_get)

class GUI_interface:
    ttk.Label(win, text="YouTube Downloader", font=("微軟正黑體", 20)).place(x=10, y=10)
    ttk.Label(win, text="輸入影片網址", font=("微軟正黑體", 14)).place(x=10, y=90)
    ttk.Entry(win, font=("微軟正黑體", 16), width=57).place(x=10, y=135)
    tk.Button(win, text="Search", font=("微軟正黑體", 13)).place(x=1116, y=135, width=154, height=184)
    ttk.Label(win, text="存檔位置 (非必填，預設為Download)", font=("微軟正黑體", 14)).place(x=10, y=220)
    ttk.Entry(win, font=("微軟正黑體", 16), width=57).place(x=10, y=265)
    ttk.Label(win, text="影片資訊", font=("微軟正黑體", 14)).place(x=10, y=350)
    ttk.Frame(win, height=5, width=1260, style="darkly").place(x=10, y=395)
    tk.Button(win, text="Download", font=("微軟正黑體", 13), command=res_set).place(x=1116, y=415, width=148, height=288)
    ttk.Frame(win, height=314, width=5, style="darkly").place(x=1095, y=395)
    ttk.Frame(win, height=314, width=5, style="darkly").place(x=925, y=395)
    tk.Label(win, text="Resolution", font=("微軟正黑體", 13)).place(x=944, y=418)
    tk.Radiobutton(win, text="Auto", font=("微軟正黑體", 13), value="Auto", variable=resolution).place(x=955, y=471)
    tk.Radiobutton(win, text="1080p", font=("微軟正黑體", 13), value="1080p", variable=resolution).place(x=955, y=531)
    tk.Radiobutton(win, text="720p", font=("微軟正黑體", 13), value="720p", variable=resolution).place(x=955, y=591)
    tk.Radiobutton(win, text="480p", font=("微軟正黑體", 13), value="480p", variable=resolution).place(x=955, y=651)

    win.mainloop()