import tkinter as tk
import openpyxl as xl
import path_test as pt

win_2 = tk.Tk()
win_2.geometry("380x260")
win_2.title("smtp/tcp settings")

global smtp, tcp, password
smtp = tk.StringVar()
tcp = tk.StringVar()
password = tk.StringVar()

direct_path = pt.path_function("/settings.xlsx")
wb = xl.load_workbook(direct_path)
sheet = wb['工作表1']

sheet['A1'].value = 'None'
sheet['A2'].value = 'None'
sheet['A3'].value = 'None'

def finish():
    global smtp_set, tcp_set, pass_set
    smtp_set = smtp.get()
    tcp_set = tcp.get()
    pass_set = password.get()

    sheet['A1'].value = smtp_set
    sheet['A2'].value = tcp_set
    sheet['A3'].value = pass_set
    print("{}, {}, {}".format(smtp_set, tcp_set, pass_set))

    wb.save(direct_path)
    win_2.destroy()

tk.Label(win_2, text="SMTP", font=("微軟正黑體", 16)).place(x=10, y=10)
tk.Entry(win_2, font=("微軟正黑體", 14), width=32, textvariable=smtp).place(x=10, y=40)
tk.Label(win_2, text="TCP", font=("微軟正黑體", 16)).place(x=10, y=70)
tk.Entry(win_2, font=("微軟正黑體", 14), width=32, textvariable=tcp).place(x=10, y=100)
tk.Label(win_2, text="Password", font=("微軟正黑體", 16)).place(x=10, y=130)
tk.Entry(win_2, font=("微軟正黑體", 14), width=32, show="*", textvariable=password).place(x=10, y=160)
tk.Button(win_2, text="finish", font=("微軟正黑體", 14), command=finish).place(x=300, y=200)

win_2.mainloop()