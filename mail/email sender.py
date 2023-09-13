from DATA import send_email_API as se
from DATA import path_test as pt
import tkinter as tk
import openpyxl

win = tk.Tk()
win.geometry("600x700")
win.title("Offline Email Sender")
win.resizable(0, 0)

global master, slave, title
master = tk.StringVar()
slave = tk.StringVar()
title = tk.StringVar()
# smtp = tk.StringVar()
# tcp = tk.StringVar()
# password = tk.StringVar()

'''
def settings():
    win_2 = tk.Tk()
    win_2.geometry("380x260")
    win_2.title("smtp/tcp settings")
    
    global smtp, tcp, password
    smtp = tk.StringVar()
    tcp = tk.StringVar()
    password = tk.StringVar()

    # global smtp_set, tcp_set, pass_set
    # smtp_set = str()
    # tcp_set = str()
    # pass_set = str()
    # smtp_set = str(smtp.get())
    # tcp_set = str(tcp.get())
    # pass_set = str(password.get())

    def finish():
        global smtp_set, tcp_set, pass_set
        smtp_set = smtp
        tcp_set = tcp
        pass_set = password
        # print("{}, {}, {}".format(smtp, tcp, password))
        print("{}, {}, {}".format(smtp_set, tcp_set, pass_set))
        win_2.destroy()

    class GUI_interface():
        tk.Label(win_2, text="SMTP", font=("微軟正黑體", 16)).place(x=10, y=10)
        tk.Entry(win_2, font=("微軟正黑體", 14), width=32, textvariable=smtp).place(x=10, y=40)
        tk.Label(win_2, text="TCP", font=("微軟正黑體", 16)).place(x=10, y=70)
        tk.Entry(win_2, font=("微軟正黑體", 14), width=32, textvariable=tcp).place(x=10, y=100)
        tk.Label(win_2, text="Password", font=("微軟正黑體", 16)).place(x=10, y=130)
        tk.Entry(win_2, font=("微軟正黑體", 14), width=32, show="*", textvariable=password).place(x=10, y=160)
        tk.Button(win_2, text="finish", font=("微軟正黑體", 14), command=finish).place(x=300, y=200)

    win_2.mainloop()
'''

def settings():
    # leb_1.pack_forget()
    print("page_2")

def email():
    result = content.get("1.0","end")
    mas = master.get()
    sla = slave.get()
    tit = title.get()
    # smtp.get()
    # tcp.get()
    # password.get()
    # if(smtp or tcp or password == ""):
    #     settings()

    # print("{}, {}, {}".format(smtp_set, tcp_set, pass_set))
    print("{}, {}, {}".format(mas, sla, tit))

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