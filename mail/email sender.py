from DATA import send_email_API as se
from DATA import path_test as pt
import tkinter as tk
import openpyxl as xl
import os

win = tk.Tk()
win.geometry("600x700")
win.title("Offline Email Sender")
win.resizable(0, 0)

def workbook():
    direct_path = pt.path_function("/settings.xlsx")
    wb = xl.load_workbook(direct_path)
    sheet = wb['工作表1']

    smtp = sheet['A1'].value
    tcp = sheet['A2'].value
    password = sheet['A3'].value
    return smtp, tcp, password   

global master, slave, title
master = tk.StringVar()
slave = tk.StringVar()
title = tk.StringVar()
# content = tk.StringVar()
# smtp = tk.StringVar()
# tcp = tk.StringVar()
# password = tk.StringVar()

def settings():
    os.system(pt.path_function("/setting.py"))

def email():
    con = content.get("1.0", "end-1c") 
    mas = master.get()
    sla = slave.get()
    tit = title.get()
    
    (smtp, tcp, password) = workbook()

    if (smtp and tcp and password == "None"):
        settings()

    se.send(mas, sla, tit, con, smtp, tcp, password)
    # print("{}, {}, {}, {}".format(mas, sla, tit, con))
    # print(smtp, tcp, password)

class GUI_interface():
    global content, leb_1, leb_2, leb_3, leb_4, ent_1, ent_2, ent_3
    leb_1 = tk.Label(win, text="Sender Address", font=("微軟正黑體", 16)).place(x=5, y=5)
    ent_1 = tk.Entry(win, font=("微軟正黑體", 14), width=45, textvariable=master).place(x=5, y=35)
    leb_2 = tk.Label(win, text="Receiver Address", font=("微軟正黑體", 16)).place(x=5, y=70)
    ent_2 = tk.Entry(win, font=("微軟正黑體", 14), width=45, textvariable=slave).place(x=5, y=100)
    leb_3 = tk.Label(win, text="title", font=("微軟正黑體", 16)).place(x=5, y=150)
    ent_3 = tk.Entry(win, font=("微軟正黑體", 14), width=53, textvariable=title).place(x=6, y=180)
    leb_4 = tk.Label(win, text="content", font=("微軟正黑體", 16)).place(x=5, y=210)
    content = tk.Text(win, font=("微軟正黑體", 12), height=10)
    content.place(x=5, y=245, width=590, height=400)
    tk.Button(win, text="smtp/tcp settings", font=("微軟正黑體", 14), command=settings).place(x=5, y=650)
    tk.Button(win, text="send", font=("微軟正黑體", 14), command=email).place(x=530, y=650)

win.mainloop()