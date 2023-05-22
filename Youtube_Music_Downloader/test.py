from pytube import YouTube
from download_path import download
import tkinter as tk
from tkinter import INSERT
from tkinter import messagebox
import ttkbootstrap as ttk

ver = str("1.0")
win = ttk.Window(themename="darkly")
win.geometry("1280x720")
win.title("YouTube Music Downloader")
win.resizable(0, 0)

global url, vid_path, vid_url, playlist, pll_title, error_list, del_list
url = tk.StringVar()
path = tk.StringVar()
vid_formate = tk.StringVar()
del_list = tk.StringVar()
playlist = []
pll_title = []
error_list = []
vid_formate.set("160kbps")

def clear():
    status_txt.delete('1.0', 'end')

def append():
    clear()
    vid_url = url.get()
    if(vid_url==""):
        messagebox.showerror("載入失敗", "未輸入網址")
        
    else:
        try:
            YT = YouTube(vid_url)
            info = YT.title
            playlist.append(vid_url)
            pll_title.append(info)
            status_txt.insert(INSERT, (info+'\n'))
        
        except:
            res = messagebox.askretrycancel("載入失敗", "無法載入網址，請檢察網址或重試")
            if(res==True):
                append()

        url.set("")

def folder(sel):
    vid_path = path.get()
    if(vid_path==""):
        vid_path = download()

    if(sel==True):
        return vid_path

def music_download():
    vid_path = folder(True)
    pl_len = len(playlist)
    if(pl_len==0):
        messagebox.showerror("下載失敗", "未載入下載列表")

    else:
        clear()
        for i in range(len(playlist)):
            try:
                status_txt.insert(INSERT, ("正在下載", pll_title[i], '\n'))
                messagebox.showinfo("正在下載", "正在下載 {}".format(pll_title[i]))
                opt = vid_formate.get()
                YT = YouTube(playlist[i])
                YT.streams.filter(type="audio", abr=opt).first().download(vid_path)
                messagebox.showinfo("作業完成", "{} 下載完成".format(pll_title[i]))
                status_txt.insert(INSERT, "下載完成", '\n')                

            except:
                error_list.append(playlist[i])
                status_txt.insert(INSERT, "{} 無法完成下載".format(pll_title[i]), '\n')

        playlist.clear()
        pll_title.clear()
        
        if(len(error_list)!=0):
            messagebox.showerror("下載失敗", "{}項作業無法完成".format(len(error_list)))

def delete():
    pre_del_list = del_list.get()
    clear()
    if(pre_del_list in playlist):
        pre_del_title = playlist.index(pre_del_list)
        playlist.remove(pre_del_list)
        pll_title.pop(pre_del_title)
        status_txt.insert(INSERT, "'{}'\n Had been removed".format(pre_del_list))
        del_list.set("")

    else:
        status_txt.insert(INSERT, "There's no such file that required to be removed.")

def DL():
    clear()
    if(len(pll_title)==0): 
        status_txt.insert(INSERT, "Download List is Empty") 

    for i in range(len(pll_title)):
        status_txt.insert(INSERT, (pll_title[i], '\n')) 

def info():
    clear()
    status_txt.insert(INSERT, "下載位置：{}".format(folder(True)))

def err_list():
    if(len(error_list)==0):
        clear()
        status_txt.insert(INSERT, "There's no Error here") 

    else:
        clear()
        status_txt.insert(INSERT, error_list)

class GUI_interface:
    global status_txt
    # ttk.Label(win, text="YouTube Music Downloader", font=("微軟正黑體", 20)).place(x=10, y=10)
    ttk.Label(win, text=("Version "+ ver), font=("微軟正黑體", 12)).place(x=1160, y=10)
    ttk.Label(win, text="輸入YouTube網址", font=("微軟正黑體", 14)).place(x=10, y=90)
    ttk.Entry(win, font=("微軟正黑體", 16), width=67, textvariable=url).place(x=10, y=137)
    tk.Button(win, text="Append", font=("微軟正黑體", 13), command=append).place(x=1116, y=131, width=154, height=62)  
    ttk.Label(win, text="下載位置 (預設為Download)", font=("微軟正黑體", 14)).place(x=10, y=220)
    ttk.Frame(win, height=192, width=5, style="darkly").place(x=695, y=204)
    
    ttk.Label(win, text="編輯下載列表", font=("微軟正黑體", 14)).place(x=713, y=220) 
    tk.Button(win, text="Delete", font=("微軟正黑體", 13), command=delete).place(x=1116, y=261, width=154, height=62)
    ttk.Entry(win, font=("微軟正黑體", 16), width=23, textvariable=del_list).place(x=713, y=268)

    ttk.Entry(win, font=("微軟正黑體", 16), width=41, textvariable=path).place(x=10, y=268)
    ttk.Label(win, text="詳細資訊", font=("微軟正黑體", 14)).place(x=10, y=350)
    ttk.Frame(win, height=5, width=1260, style="darkly").place(x=10, y=395)
    tk.Button(win, text="Download", font=("微軟正黑體", 13), command=music_download).place(x=1116, y=415, width=148, height=288)
    ttk.Frame(win, height=315, width=5, style="darkly").place(x=1095, y=395)
    ttk.Frame(win, height=315, width=5, style="darkly").place(x=831, y=395)
    tk.Label(win, text="Format", font=("微軟正黑體", 13)).place(x=847, y=420)
    tk.Radiobutton(win, text="mp4 - 48kbps", font=("微軟正黑體", 13), value="48kbps", variable=vid_formate).place(x=847, y=471)
    tk.Radiobutton(win, text="mp4 - 128kbps", font=("微軟正黑體", 13), value="128kbps", variable=vid_formate).place(x=847, y=531)
    tk.Radiobutton(win, text="webm - 50kbps", font=("微軟正黑體", 13), value="50kbps", variable=vid_formate).place(x=847, y=591)
    tk.Radiobutton(win, text="webm - 160kbps", font=("微軟正黑體", 13), value="160kbps", variable=vid_formate).place(x=847, y=651)
    status_txt = tk.Text(win, font=("微軟正黑體", 12))
    status_txt.place(x=15, y=413, width=803, height=220)
    tk.Button(win, text="Download List", font=("微軟正黑體", 13), command=DL).place(x=15, y=645, width=168, height=62)
    tk.Button(win, text="Path Info", font=("微軟正黑體", 13), command=info).place(x=195, y=645, width=154, height=62)
    tk.Button(win, text="Error List", font=("微軟正黑體", 13), command=err_list).place(x=360, y=645, width=154, height=62)
    tk.Button(win, text="Clear", font=("微軟正黑體", 13), command=clear).place(x=664, y=645, width=154, height=62)
    
    win.mainloop()