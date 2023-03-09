import tkinter as tk
import ttkbootstrap as ttk
from PIL import Image, ImageTk
import os
import pyautogui

width, height = pyautogui.size()
if (width>1920 and height>1080):
    screensize = ("500x500")

else:
    screensize = ("350x410")

win = ttk.Window(themename="litera")
win.geometry(screensize)
win.resizable(0, 0)
win.title("ARCS Function Menu")

def path():
    file_path = os.path.abspath(os.path.dirname(__file__))
    length = len(file_path)
    file_path_2 = []
    for i in range(0, length):       
        if file_path[i] == "\\":
            file_path_2.append("/")

        else :
            file_path_2.append(file_path[i])

    return (file_path_2)

def save_button():
    os._exit(False)

pic_path = path()
pic_path.append("/K3S12.png")
pic_path = "".join(pic_path)
pic_logo = Image.open(pic_path)
pic = ImageTk.PhotoImage(pic_logo)
tk.Label(win, text="Function Menu 功能列表", font=("微軟正黑體", 20)).pack(anchor=tk.NW, padx=10, pady=5)
tk.Label(win, image=pic).pack(side=tk.BOTTOM, anchor=tk.SW, padx=10, pady=10)

tk.Checkbutton(win, text="Auto Attending 自動上課", font=("微軟正黑體", 14)).pack(anchor=tk.NW, padx=10, pady=5)
tk.Checkbutton(win, text="Auto Dismissing 自動下課", font=("微軟正黑體", 14)).pack(anchor=tk.NW, padx=10, pady=5)
tk.Checkbutton(win, text="Windows Mute 視窗自動靜音", font=("微軟正黑體", 14)).pack(anchor=tk.NW, padx=10, pady=5)
tk.Checkbutton(win, text="Mic Mute 麥克風自動靜音", font=("微軟正黑體", 14)).pack(anchor=tk.NW, padx=10, pady=5)
tk.Checkbutton(win, text="Camera Off 鏡頭自動關閉", font=("微軟正黑體", 14)).pack(anchor=tk.NW, padx=10, pady=5)
tk.Button(win, text="Save 儲存", font=("微軟正黑體", 14), command=save_button).pack(anchor=tk.NW, padx=10, pady=5)

win.mainloop()