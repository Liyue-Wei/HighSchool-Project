from pytube import YouTube
# from download_path import download
import tkinter as tk
from tkinter import INSERT
# from tkinter import messagebox
import ttkbootstrap as ttk
# import os

win = ttk.Window(themename="darkly")
win.geometry("1280x720")
win.title("YouTube Music")
win.resizable(0, 0)

global url, vid_path, vid_url, playlist, pll_title, error_list
url = tk.StringVar()
path = tk.StringVar()
playlist = []
pll_title = []
error_list = []

def append():
    vid_url = url.get()
    YT = YouTube(vid_url)
    info = YT.title
    playlist.append(YT)
    pll_title.append(info)
    status_txt.insert(INSERT, (info+'\n'))

def delete():
    status_txt.delete('1.0', 'end')

def video_download():
    vid_path = path.get()
    # vid_path = download()

'''
    if vid_url == "":
        messagebox.showerror("下載失敗", "未輸入網址")

    else:
        try:
            YT = YouTube(vid_url)
            status_txt.insert(INSERT, YT.title)
            try:
                YT.streams.filter(type="audio", audio_codec="opus").last().download()
                status_txt.insert(INSERT, YT.title())

            except:
                messagebox.showerror("下載失敗", "影片無法下載")
        
        except:
            messagebox.showerror("下載失敗", "查無此影片")
'''

class GUI_interface:
    global status_txt
    ttk.Label(win, text="YouTube Music Downloader", font=("微軟正黑體", 20)).place(x=10, y=10)
    ttk.Label(win, text="輸入YouTube網址", font=("微軟正黑體", 14)).place(x=10, y=90)
    ttk.Entry(win, font=("微軟正黑體", 16), width=67, textvariable=url).place(x=10, y=135)
    tk.Button(win, text="Append", font=("微軟正黑體", 13), command=append).place(x=1116, y=131, width=154, height=62)
    ttk.Label(win, text="下載位置 (預設為Download)", font=("微軟正黑體", 14)).place(x=10, y=220)
    tk.Button(win, text="Select", font=("微軟正黑體", 13)).place(x=528, y=261, width=154, height=62)
    ttk.Frame(win, height=192, width=5, style="darkly").place(x=695, y=204)
    ttk.Label(win, text="編輯預下載列表", font=("微軟正黑體", 14)).place(x=713, y=220)
    tk.Button(win, text="Delete", font=("微軟正黑體", 13), command=delete).place(x=1116, y=261, width=154, height=62)
    tk.Radiobutton(win, text="由網址刪除", font=("微軟正黑體", 11)).place(x=713, y=340)
    tk.Radiobutton(win, text="由歌名刪除", font=("微軟正黑體", 11)).place(x=884, y=340)
    tk.Radiobutton(win, text="由錯誤自動刪除", font=("微軟正黑體", 11)).place(x=1055, y=340)
    ttk.Entry(win, font=("微軟正黑體", 16), width=30).place(x=10, y=265)
    ttk.Entry(win, font=("微軟正黑體", 16), width=23).place(x=713, y=265)
    ttk.Label(win, text="詳細資訊", font=("微軟正黑體", 14)).place(x=10, y=350)
    ttk.Frame(win, height=5, width=1260, style="darkly").place(x=10, y=395)
    tk.Button(win, text="Download", font=("微軟正黑體", 13), command=video_download).place(x=1116, y=415, width=148, height=288)
    ttk.Frame(win, height=315, width=5, style="darkly").place(x=1095, y=395)
    ttk.Frame(win, height=315, width=5, style="darkly").place(x=831, y=395)
    tk.Label(win, text="Format", font=("微軟正黑體", 13)).place(x=847, y=420)
    tk.Radiobutton(win, text="mp4 - 48kbps", font=("微軟正黑體", 13)).place(x=847, y=471)
    tk.Radiobutton(win, text="mp4 - 128kbps", font=("微軟正黑體", 13)).place(x=847, y=531)
    tk.Radiobutton(win, text="webm - 50kbps", font=("微軟正黑體", 13)).place(x=847, y=591)
    tk.Radiobutton(win, text="webm - 160kbps", font=("微軟正黑體", 13)).place(x=847, y=651)
    status_txt = tk.Text(win, font=("微軟正黑體", 12))
    status_txt.place(x=15, y=413, width=803, height=290)

    win.mainloop()
