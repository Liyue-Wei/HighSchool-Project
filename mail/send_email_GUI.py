from send_email_API import send
import tkinter as tk

win = tk.Tk()
win.geometry("1280x720")
win.title("Email sender")
win.resizable(0, 0)

global master, slave, title, content, smtp, tcp, password

win.mainloop()