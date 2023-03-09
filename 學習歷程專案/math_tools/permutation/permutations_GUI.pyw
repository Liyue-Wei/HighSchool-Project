import ttkbootstrap as ttk
import tkinter as tk
from math import factorial

win = ttk.Window(themename="litera")

win.geometry("1400x1350")
win.resizable(0, 0)
win.title("permutations caculator")

def C():
    n = int(C_n.get())
    k = int(C_k.get())

    if(n-k<0):
        C_ans.set("False")
    
    def P(n, k):
        ans = factorial(n)/factorial(n-k)
        return ans

    c_ans = P(n, k)/factorial(k)
    C_ans.set(int(c_ans))

def P():
    n = int(P_n.get())
    k = int(P_k.get())
    
    if(n-k<0):
        P_ans.set("False")

    p_ans = factorial(n)/factorial(n-k)
    P_ans.set(int(p_ans))
    
def U():
    n = int(U_n.get())
    k = int(U_k.get())
    
    if(n-k<0):
        U_ans.set("False")

    u_ans = n**k
    U_ans.set(int(u_ans))

def H():
    n = int(H_n.get())
    k = int(H_k.get())

    if(n-k<0):
        H_ans.set("False")

    def C(n, k):
        def P(n, K):
            ans = factorial(n)/factorial(n-k)
            return ans

        ans_2 = P(n, k)/factorial(k)
        return ans_2

    h_ans = C(n+k-1, k)
    H_ans.set(int(h_ans))

def fac():
    n = int(fac_n.get())
    ans = factorial(n)

    fac_ans.set(int(ans))

class GUI_interface:
    label_1 = ttk.Label(win, text="排列組合計算機", style="litera", font=("微軟正黑體", 24)).place(x=15, y=10)
    
    class permutation_geomentary_parameter:
        global x_def, y_def, CPUH_height, CPUH_width, entry_height, entry_width, label_2_height, switch_height
        x_def = 20
        y_def = 120
        CPUH_width = 180
        CPUH_height = 10
        entry_width = 125
        entry_height = 120
        label_2_height = 100
        switch_height = 250

    class caculator_geomentary:
        global entry_x, entry_y, num_button_x, num_button_y, num_button_width, num_button_height
        
    class C:
        global C_n, C_k, C_ans
        C_n = tk.StringVar()
        C_k = tk.StringVar()
        C_ans = tk.StringVar()

        label_C_1 = ttk.Label(win, text="C", style="litera", font=("微軟正黑體", 68)).place(x=x_def, y=y_def)
        entry_C_1 = ttk.Entry(win, style="litera", font=("微軟正黑體", 16), width="4", textvariable=C_n).place(x=x_def+CPUH_width, y=y_def+CPUH_height)
        entry_C_2 = ttk.Entry(win, style="litera", font=("微軟正黑體", 16), width="4", textvariable=C_k).place(x=x_def+CPUH_width, y=y_def+CPUH_height+entry_height)
        label_C_2 = ttk.Label(win, text="=", style="litera", font=("微軟正黑體", 68)).place(x=x_def+CPUH_width+entry_width, y=label_2_height)
        label_C_3 = ttk.Label(win, style="litera", font=("微軟正黑體", 68), textvariable=C_ans).place(x=x_def+CPUH_width+entry_width+150, y=label_2_height+20)
        button_C_1 = tk.Button(win, text="Count", font=("微軟正黑體", 14), command=C).place(x=1400-170, y=label_2_height+85)
    
    class P:
        global P_n, P_k, P_ans
        P_n = tk.StringVar()
        P_k = tk.StringVar()
        P_ans = tk.StringVar()

        label_P_1 = ttk.Label(win, text="P", style="litera", font=("微軟正黑體", 68)).place(x=x_def, y=y_def+switch_height)
        entry_P_1 = ttk.Entry(win, style="litera", font=("微軟正黑體", 16), width="4", textvariable=P_n).place(x=x_def+CPUH_width, y=y_def+CPUH_height+switch_height)
        entry_P_2 = ttk.Entry(win, style="litera", font=("微軟正黑體", 16), width="4", textvariable=P_k).place(x=x_def+CPUH_width, y=y_def+CPUH_height+entry_height+switch_height)
        label_P_2 = ttk.Label(win, text="=", style="litera", font=("微軟正黑體", 68)).place(x=x_def+CPUH_width+entry_width, y=label_2_height+switch_height)
        label_P_3 = ttk.Label(win, style="litera", font=("微軟正黑體", 68), textvariable=P_ans).place(x=x_def+CPUH_width+entry_width+150, y=label_2_height+switch_height+20)
        button_P_1 = tk.Button(win, text="Count", font=("微軟正黑體", 14), command=P).place(x=1400-170, y=label_2_height+85+switch_height)

    class U:
        global U_n, U_k, U_ans
        U_n = tk.StringVar()
        U_k = tk.StringVar()
        U_ans = tk.StringVar()

        label_U_1 = ttk.Label(win, text="U", style="litera", font=("微軟正黑體", 68)).place(x=x_def, y=y_def+2*switch_height)
        entry_U_1 = ttk.Entry(win, style="litera", font=("微軟正黑體", 16), width="4", textvariable=U_n).place(x=x_def+CPUH_width, y=y_def+CPUH_height+2*switch_height)
        entry_U_2 = ttk.Entry(win, style="litera", font=("微軟正黑體", 16), width="4", textvariable=U_k).place(x=x_def+CPUH_width, y=y_def+CPUH_height+entry_height+2*switch_height)
        label_U_2 = ttk.Label(win, text="=", style="litera", font=("微軟正黑體", 68)).place(x=x_def+CPUH_width+entry_width, y=label_2_height+2*switch_height)
        label_U_3 = ttk.Label(win, style="litera", font=("微軟正黑體", 68), textvariable=U_ans).place(x=x_def+CPUH_width+entry_width+150, y=label_2_height+2*switch_height+20)
        button_U_1 = tk.Button(win, text="Count", font=("微軟正黑體", 14), command=U).place(x=1400-170, y=label_2_height+85+switch_height*2)

    class H:
        global H_n, H_k, H_ans
        H_n = tk.StringVar()
        H_k = tk.StringVar()
        H_ans = tk.StringVar()

        label_H_1 = ttk.Label(win, text="H", style="litera", font=("微軟正黑體", 68)).place(x=x_def, y=y_def+3*switch_height)
        entry_H_1 = ttk.Entry(win, style="litera", font=("微軟正黑體", 16), width="4", textvariable=H_n).place(x=x_def+CPUH_width, y=y_def+CPUH_height+3*switch_height)
        entry_H_2 = ttk.Entry(win, style="litera", font=("微軟正黑體", 16), width="4", textvariable=H_k).place(x=x_def+CPUH_width, y=y_def+CPUH_height+entry_height+3*switch_height)
        label_H_2 = ttk.Label(win, text="=", style="litera", font=("微軟正黑體", 68)).place(x=x_def+CPUH_width+entry_width, y=label_2_height+3*switch_height)
        label_H_3 = ttk.Label(win, style="litera", font=("微軟正黑體", 68), textvariable=H_ans).place(x=x_def+CPUH_width+entry_width+150, y=label_2_height+3*switch_height+20)
        button_H_1 = tk.Button(win, text="Count", font=("微軟正黑體", 14), command=H).place(x=1400-170, y=label_2_height+85+switch_height*3)
    
    class factorial:
        global fac_n, fac_ans
        fac_n = tk.StringVar()
        fac_ans = tk.StringVar()

        label_fac_1 = ttk.Label(win, text="n!", style="litera", font=("微軟正黑體", 68)).place(x=x_def, y=y_def+4*switch_height)
        entry_fac_1 = ttk.Entry(win, style="litera", font=("微軟正黑體", 16), width="4", textvariable=fac_n).place(x=x_def+CPUH_width, y=y_def+CPUH_height+4.275*switch_height)
        label_fac_2 = ttk.Label(win, text="=", style="litera", font=("微軟正黑體", 68)).place(x=x_def+CPUH_width+entry_width, y=label_2_height+4*switch_height+15)
        label_fac_3 = ttk.Label(win, style="litera", font=("微軟正黑體", 68), textvariable=fac_ans).place(x=x_def+CPUH_width+entry_width+150, y=label_2_height+4*switch_height+20)
        button_fac_1 = tk.Button(win, text="Count", font=("微軟正黑體", 14), command=fac).place(x=1400-170, y=label_2_height+85+switch_height*4)
    
win.mainloop()