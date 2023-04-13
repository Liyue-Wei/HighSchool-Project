from pytube import YouTube
import tkinter as tk
from tkinter import INSERT
from tkinter import messagebox
import ttkbootstrap as ttk

win = ttk.Window(themename="darkly")
win.geometry("1280x595")
win.title("YouTube Music")
win.resizable(0, 0)

global url
url = tk.StringVar()
path = tk.StringVar()

def delete():
    status_txt.delete('1.0', 'end')

# def video_download():

class GUI_interface:
    global status_txt
    ttk.Label(win, text="YouTube Music Downloader", font=("微軟正黑體", 20)).place(x=10, y=10)
    ttk.Label(win, text="輸入YouTube網址", font=("微軟正黑體", 14)).place(x=10, y=90)
    ttk.Entry(win, font=("微軟正黑體", 16), width=67, textvariable=url).place(x=10, y=137)
    tk.Button(win, text="Search", font=("微軟正黑體", 13)).place(x=1116, y=131, width=154, height=62)
    ttk.Label(win, text="詳細資訊", font=("微軟正黑體", 14)).place(x=10, y=225)
    ttk.Frame(win, height=5, width=1260, style="darkly").place(x=10, y=270)
    tk.Button(win, text="Download", font=("微軟正黑體", 13)).place(x=1116, y=290, width=148, height=288)
    ttk.Frame(win, height=315, width=5, style="darkly").place(x=1095, y=270)
    ttk.Frame(win, height=315, width=5, style="darkly").place(x=831, y=270)
    tk.Label(win, text="Format", font=("微軟正黑體", 13)).place(x=847, y=295)
    tk.Radiobutton(win, text="mp4 - 48kbps", font=("微軟正黑體", 13)).place(x=847, y=346)
    tk.Radiobutton(win, text="mp4 - 128kbps", font=("微軟正黑體", 13)).place(x=847, y=408)
    tk.Radiobutton(win, text="webm - 50kbps", font=("微軟正黑體", 13)).place(x=847, y=466)
    tk.Radiobutton(win, text="webm - 160kbps", font=("微軟正黑體", 13)).place(x=847, y=526)
    status_txt = tk.Text(win, font=("微軟正黑體", 12))
    status_txt.place(x=15, y=288, width=803, height=290)

    win.mainloop()