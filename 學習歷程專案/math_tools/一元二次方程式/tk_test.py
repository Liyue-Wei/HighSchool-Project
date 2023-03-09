import tkinter as tk
win = tk.Tk()
win.geometry("1280x720")
win.title("test")

label1 = tk.Label(win, text="test", fg='black')
label1.pack()

win.mainloop()