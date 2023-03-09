import ttkbootstrap as ttk
import tkinter as tk
from PIL import Image, ImageTk
import time
import os
import pyautogui

width, height = pyautogui.size()
if (width>1920 and height>1080):
    screensize = ("1280x720")

else:
    screensize = ("1000x525")

win = ttk.Window(themename="minty")
win.geometry(screensize)
win.resizable(0, 0)
win.title("ARCS By K3S12")

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

def menu():   
    file_path = path()
    file_path.append("/User_DATA/ARCS_menu.pyw")
    file_path = "".join(file_path)
    os.system(file_path)

def guide():
    file_path = path()   
    file_path.append("/User_DATA/ARCS_User's_Guide.docx")
    file_path = "".join(file_path)
    os.system(file_path)  

def Ch_Ver():
    file_path = path()
    file_path.append("/ARCS_GUI_interface.pyw")
    file_path = "".join(file_path)
    os.system(file_path)

class GUI_interface:
    pic_path = path()
    pic_path.append("/User_DATA/K3S12.png")
    pic_path = "".join(pic_path)
    pic_logo = Image.open(pic_path)
    pic = ImageTk.PhotoImage(pic_logo)
    tk.Label(win, text="Online Course Auto Roll Call System", font=("微軟正黑體", 24)).pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)
    tk.Label(win, text="Developed by K3S12 Python Studio", font=("微軟正黑體", 12)).pack(anchor=tk.NE, padx=10, pady=0)
    tk.Label(win, image=pic).pack(side=tk.BOTTOM, anchor=tk.SE, padx=10, pady=10)

    tk.Label(win, text=(time.strftime("%d/%m/%Y  %H:%M:%S", time.localtime())+"    non-school hour now"), font=("微軟正黑體", 16)).pack(anchor=tk.SE, padx=10, pady=0)

    tk.Button(win, text="Attend Class", font=("微軟正黑體", 16)).pack(anchor=tk.W, fill=tk.BOTH, padx=10, pady=10, ipady=10)
    tk.Button(win, text="Quick Links to Current Courses (Google Classroom)", font=("微軟正黑體", 16)).pack(anchor=tk.W, fill=tk.BOTH, padx=10, pady=10, ipady=10)
    
    tk.Label(win, text=" ", font=("微軟正黑體", 16)).pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)  
    tk.Label(win, text=" Edit & Options", font=("微軟正黑體", 14)).pack(anchor=tk.W, padx=10, pady=0, ipady=10)
    tk.Button(win, text="Edit Links", font=("微軟正黑體", 14)).pack(side=tk.LEFT, anchor=tk.N, padx=10, pady=10, ipady=5)
    tk.Button(win, text="Edit Schedule", font=("微軟正黑體", 14)).pack(side=tk.LEFT, anchor=tk.N, padx=10, pady=10, ipady=5)
    tk.Button(win, text="Change Account", font=("微軟正黑體", 14)).pack(side=tk.LEFT, anchor=tk.N, padx=10, pady=10, ipady=5)
    tk.Button(win, text="User's Guide", font=("微軟正黑體", 14), command=guide).pack(side=tk.LEFT, anchor=tk.N, padx=10, pady=10, ipady=5)
    tk.Button(win, text="中文版", font=("微軟正黑體", 14), command=Ch_Ver).pack(side=tk.LEFT, anchor=tk.N, padx=10, pady=10, ipady=5)
    tk.Button(win, text="Function Menu", font=("微軟正黑體", 14), command=menu).pack(anchor=tk.N, padx=10, pady=10, fill=tk.X, ipady=5)

win.mainloop() 