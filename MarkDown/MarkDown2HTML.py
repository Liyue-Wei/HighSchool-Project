# import tkinter as tk
# from tkinter import messagebox
import markdown
import codecs
import os

global file_name
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

def path_function():
    file_path = path()
    direct_path = ("/"+str(file_name.get()))
    file_path.append(direct_path)
    file_path = "".join(file_path)
    return(file_path)

def convert():
    try:
        file_input = codecs.open((str(path_function())+".md"), mode="r", encoding="utf-8")
        md_text = file_input.read()
        html_text = markdown.markdown(md_text)
        file_output = codecs.open((str(file_name.get())+".html"), mode="w", encoding="utf-8")
        file_output.write(html_text)
        
        print("完成")
        # messagebox.showinfo(title="Compelete", message="完成")

    except:
        print("查無此文件")
        # messagebox.showerror(title="Error", message="查無此文件")

file_name = input()
convert()

'''
win = tk.Tk()
win.geometry("700x148")
win.title("MarkDown 2 HTML")

global file_name
file_name = tk.StringVar()

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

def path_function():
    file_path = path()
    direct_path = ("/"+str(file_name.get()))
    file_path.append(direct_path)
    file_path = "".join(file_path)
    return(file_path)

def convert():
    try:
        file_input = codecs.open((str(path_function())+".md"), mode="r", encoding="utf-8")
        md_text = file_input.read()
        html_text = markdown.markdown(md_text)
        file_output = codecs.open((str(file_name.get())+".html"), mode="w", encoding="utf-8")
        file_output.write(html_text)
        
        messagebox.showinfo(title="Compelete", message="完成")

    except:
        messagebox.showerror(title="Error", message="查無此文件")

tk.Label(win, text="MarkDown to HTML", font=("微軟正黑體", 20)).pack(side=tk.TOP, anchor=tk.NW, padx=5, pady=5)
tk.Label(win, text="Input MarkDown file name", font=("微軟正黑體", 16)).pack(anchor=tk.NW, padx=5, pady=10)
tk.Entry(win, text="file name", font=("微軟正黑體", 16), width=52, textvariable=file_name).pack(side=tk.LEFT, anchor=tk.N, padx=5, pady=0, ipady=3)
tk.Button(win, text="Enter", font=("微軟正黑體", 12), command=convert).pack(side=tk.LEFT, anchor=tk.N, padx=5, pady=0)

win.mainloop()
'''