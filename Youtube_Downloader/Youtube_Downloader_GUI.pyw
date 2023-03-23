from pytube import YouTube
import tkinter as tk
import ttkbootstrap as ttk
import os

win = ttk.Window(themename="darkly")
win.geometry("1280x720")
win.title("YouTube Downloader")
win.resizable(0, 0)

class GUI_interface:
    ttk.Label(win, text="YouTube Downloader", font=("微軟正黑體", 20)).place(x=10, y=10)
    ttk.Label(win, text="輸入影片網址", font=("微軟正黑體", 14)).place(x=10, y=90)
    ttk.Entry(win, font=("微軟正黑體", 16), width=57).place(x=10, y=135)
    tk.Button(win, text="Search", font=("微軟正黑體", 13)).place(x=1116, y=135, width=154, height=184)
    ttk.Label(win, text="存檔位置 (非必填，預設為Download)", font=("微軟正黑體", 14)).place(x=10, y=220)
    ttk.Entry(win, font=("微軟正黑體", 16), width=57).place(x=10, y=265)
    ttk.Label(win, text="影片資訊", font=("微軟正黑體", 14)).place(x=10, y=350)
    ttk.Frame(win, height=5, width=1260, style="darkly").place(x=10, y=395)
    tk.Button(win, text="Download", font=("微軟正黑體", 13)).place(x=1116, y=415, width=148, height=288)
    ttk.Frame(win, height=314, width=5, style="darkly").place(x=1095, y=395)
    ttk.Frame(win, height=314, width=5, style="darkly").place(x=925, y=395)
    tk.Radiobutton(win, text="Best", font=("微軟正黑體", 13)).place(x=955, y=415)
    tk.Radiobutton(win, text="1080p", font=("微軟正黑體", 13)).place(x=955, y=475)
    tk.Radiobutton(win, text="720p", font=("微軟正黑體", 13)).place(x=955, y=535)
    tk.Radiobutton(win, text="480p", font=("微軟正黑體", 13)).place(x=955, y=595)
    tk.Radiobutton(win, text="144p", font=("微軟正黑體", 13)).place(x=955, y=655)
    tk.Text(win, state="disabled").place(x=14, y=415, width=897, height=288)

    win.mainloop()