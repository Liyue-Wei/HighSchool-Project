from send_email_API import send
import tkinter as tk

win = tk.Tk()
win.geometry("600x700")
win.title("Offline Email Sender")
win.resizable(0, 0)

global master, slave, title, content, smtp, tcp, password
master = tk.StringVar()
slave = tk.StringVar()
title = tk.StringVar()
# content = tk.StringVar()
smtp = tk.StringVar()
tcp = tk.StringVar()
password = tk.StringVar()

def settings():
    print("hello world")

def email():
    print("send")

class GUI_interface():
    tk.Label(win, text="Sender Address", font=("微軟正黑體", 16)).place(x=5, y=5)
    tk.Entry(win, font=("微軟正黑體", 14), width=45, textvariable=master).place(x=5, y=35)
    tk.Label(win, text="Receiver Address", font=("微軟正黑體", 16)).place(x=5, y=70)
    tk.Entry(win, font=("微軟正黑體", 14), width=45, textvariable=slave).place(x=5, y=100)
    tk.Label(win, text="title", font=("微軟正黑體", 16)).place(x=5, y=150)
    tk.Entry(win, font=("微軟正黑體", 14), width=50, textvariable=title).place(x=5, y=180)
    tk.Label(win, text="content", font=("微軟正黑體", 16)).place(x=5, y=210)
    content = tk.Text(win, font=("微軟正黑體", 12)).place(x=5, y=245, width=590, height=400)
    tk.Button(win, text="smtp/tcp settings", font=("微軟正黑體", 14), command=settings).place(x=5, y=650)
    tk.Button(win, text="send", font=("微軟正黑體", 14), command=email).place(x=530, y=650)

win.mainloop()